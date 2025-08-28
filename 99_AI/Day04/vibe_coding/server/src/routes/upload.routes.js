const express = require('express');
const router = express.Router();
const uploadController = require('../controllers/upload.controller');

// The uploadMiddleware will handle the file upload
// The uploadImage controller will then send the response
router.post('/', uploadController.uploadMiddleware, uploadController.uploadImage);

module.exports = router;
