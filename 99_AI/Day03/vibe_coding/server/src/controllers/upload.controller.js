const multer = require('multer');
const path = require('path');

// Configure multer for file storage
const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, 'src/uploads/');
  },
  filename: function (req, file, cb) {
    const uniqueSuffix = Date.now() + '-' + Math.round(Math.random() * 1E9);
    cb(null, file.fieldname + '-' + uniqueSuffix + path.extname(file.originalname));
  }
});

const upload = multer({ storage: storage });

const uploadImage = (req, res) => {
  if (!req.file) {
    return res.status(400).json({ error: 'No file uploaded.' });
  }

  // Return the path to the uploaded file
  // The path should be relative to the server's public serving directory
  res.status(200).json({ filePath: `/uploads/${req.file.filename}` });
};

module.exports = {
  uploadMiddleware: upload.single('image'), // 'image' is the field name
  uploadImage,
};
