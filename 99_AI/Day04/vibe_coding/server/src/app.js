const express = require('express');
const cors = require('cors');
const path = require('path'); // Add path module
const corsOptions = require('./config/cors');

const app = express();

app.use(cors(corsOptions));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Serve uploaded files statically
app.use('/uploads', express.static(path.join(__dirname, 'uploads')));

app.get('/', (req, res) => {
  res.send('SSAFY AI Chatbot Server is running!');
});

const chatRoutes = require('./routes/chat.routes.js');
const authRoutes = require('./routes/auth.routes.js');
const uploadRoutes = require('./routes/upload.routes.js');

app.use('/api/chat', chatRoutes);
app.use('/api/auth', authRoutes);
app.use('/api/upload', uploadRoutes);

module.exports = app;
