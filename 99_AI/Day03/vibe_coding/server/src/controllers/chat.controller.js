const openaiService = require('../services/openai.service');

const handleChat = async (req, res) => {
  try {
    const { input, imageUrl } = req.body;
    if (!input) {
      return res.status(400).json({ error: 'Input is required' });
    }

    const aiResponse = await openaiService.getChatCompletion(input, imageUrl);

    res.json({ output_text: aiResponse });
  } catch (error) {
    console.error('Error in chat controller:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
};

module.exports = { handleChat };
