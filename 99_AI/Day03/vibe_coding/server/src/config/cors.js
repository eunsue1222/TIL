const env = require('./env');

const corsOptions = {
  origin: env.corsOrigin,
  optionsSuccessStatus: 200,
};

module.exports = corsOptions;
