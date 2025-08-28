require('dotenv').config();

module.exports = {
  port: process.env.PORT,
  openaiApiKey: process.env.OPENAI_API_KEY,
  corsOrigin: process.env.CORS_ORIGIN,
};
