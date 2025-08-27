const express = require('express');
const router = express.Router();

// Placeholder for auth controller
const authController = {
    login: (req, res) => res.status(501).json({ message: 'Not Implemented' }),
    register: (req, res) => res.status(501).json({ message: 'Not Implemented' }),
};

router.post('/login', authController.login);
router.post('/register', authController.register);

module.exports = router;
