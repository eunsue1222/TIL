require('dotenv').config();
const express = require('express');
const cors = require('cors');

// Note: 'openai' package is not installed yet. This is a placeholder.
// const OpenAI = require('openai');

const app = express();
const port = process.env.PORT || 3001;

// Middleware
app.use(cors({ origin: process.env.CORS_ORIGIN || 'http://localhost:5173' }));
app.use(express.json());

// API Endpoints

// Placeholder for OpenAI client
// const openai = new OpenAI({
//   apiKey: process.env.OPENAI_API_KEY,
// });

app.get('/', (req, res) => {
    res.send('SSAFY AI Chatbot Server is running!');
});

app.post('/api/chat', async (req, res) => {
    // const { message, image } = req.body; // Assuming message and optional image
    
    try {
        // const response = await openai.responses.create({
        //     model: "gpt-5-nano", // As specified in PRD, though this model might not exist
        //     input: [{
        //         role: "user",
        //         content: [
        //             { type: "input_text", text: message },
        //             // Add image logic here if an image is present
        //         ],
        //     }],
        // });
        // res.json({ reply: response.output_text });

        // Using placeholder response for now
        res.json({ reply: "This is a placeholder response from the AI." });

    } catch (error) {
        console.error('Error calling OpenAI API:', error);
        res.status(500).json({ error: 'Failed to get response from AI' });
    }
});

app.post('/api/upload', (req, res) => {
    // Logic for image upload will be implemented here
    res.status(501).json({ message: 'Not Implemented' });
});

app.post('/api/login', (req, res) => {
    // Logic for user login
    res.status(501).json({ message: 'Not Implemented' });
});

app.post('/api/register', (req, res) => {
    // Logic for user registration
    res.status(501).json({ message: 'Not Implemented' });
});


// Basic Error Handling
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).send('Something broke!');
});

app.listen(port, () => {
    console.log(`Server listening at http://localhost:${port}`);
});
