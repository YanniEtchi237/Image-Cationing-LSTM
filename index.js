// backend/server.js
const express = require('express');
const multer  = require('multer');
const { spawn } = require('child_process');

const app = express();
const port = 3001;

const upload = multer({ dest: 'uploads/' });

// Define route to handle file uploads
app.post('/upload', upload.single('image'), (req, res) => {
  const imagePath = req.file.path;

  // Spawn a child process to run the Python prediction script
  const pythonProcess = spawn('python', ['predict.py', imagePath]);

  pythonProcess.stdout.on('data', (data) => {
    console.log(`Python stdout: ${data}`);
    res.json({ prediction: data.toString() });
  });

  pythonProcess.stderr.on('data', (data) => {
    console.error(`Python stderr: ${data}`);
    res.status(500).send('Error processing image');
  });
});

// Start the server
app.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`);
});

