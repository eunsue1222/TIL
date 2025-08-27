const app = require('./app');
const env = require('./config/env');

const PORT = env.port || 3001;

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
