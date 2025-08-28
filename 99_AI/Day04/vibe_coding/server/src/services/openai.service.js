const OpenAI = require('openai');
const env = require('../config/env');
const fs = require('fs');
const path = require('path');
const mime = require('mime-types');

const getChatCompletion = async (userInput, imageUrl) => {
  if (!env.openaiApiKey) {
    return 'API키가 없습니다.';
  }

  const openai = new OpenAI({
    apiKey: env.openaiApiKey,
  });

  try {
    let content = userInput;

    if (imageUrl) {
      const url = new URL(imageUrl);
      const filename = path.basename(url.pathname);
      const localPath = path.join(__dirname, '../uploads', filename);

      if (fs.existsSync(localPath)) {
        const fileBuffer = fs.readFileSync(localPath);
        const base64Image = fileBuffer.toString('base64');
        const mimeType = mime.lookup(localPath) || 'image/jpeg';
        const dataUri = `data:${mimeType};base64,${base64Image}`;

        content = [
          { type: 'text', text: userInput },
          { type: 'image_url', image_url: { url: dataUri } },
        ];
      } else {
        console.warn(`Image file not found at path: ${localPath}. Proceeding without image.`);
      }
    }

    const response = await openai.chat.completions.create({
      model: 'gpt-5-nano',
      messages: [{ role: 'user', content }],
    });
    return response.choices[0].message.content;
  } catch (error) {
    console.error('Error calling OpenAI API:', error);
    throw error;
  }
};

module.exports = { getChatCompletion };
