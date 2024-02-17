// frontend/script.js
document.getElementById('fileDropArea').addEventListener('click', () => {
  document.getElementById('fileInput').click();
});

document.getElementById('fileInput').addEventListener('change', (event) => {
  const file = event.target.files[0];
  if (file) {
    
    document.querySelector('.file-drop-text').textContent = file.name; // Update text to show the file name
  }
});

// Drag and drop events
const fileDropArea = document.getElementById('fileDropArea');

fileDropArea.addEventListener('dragenter', (event) => {
  event.preventDefault();
  fileDropArea.classList.add('dragover');
});

fileDropArea.addEventListener('dragover', (event) => {
  event.preventDefault();
  fileDropArea.classList.add('dragover');
});

fileDropArea.addEventListener('dragleave', () => {
  fileDropArea.classList.remove('dragover');
});

fileDropArea.addEventListener('drop', (event) => {
  event.preventDefault();
  fileDropArea.classList.remove('dragover');

  const file = event.dataTransfer.files[0];
  if (file) {
    document.querySelector('.file-drop-text').textContent = file.name; // Update text to show the file name
  }
});

document.getElementById('uploadButton').addEventListener('click', () => {
  const fileInput = document.getElementById('fileInput');
  const file = fileInput.files[0];
  if (file) {
    uploadFile(file);
  } else {
    alert('Please select an image file.');
  }
});



document.getElementById('uploadButton').addEventListener('click', () => {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];
    if (file) {
      uploadFile(file);
    } else {
      alert('Please select an image file.');
    }
  });
  
  function uploadFile(file) {
    const formData = new FormData();
    formData.append('image', file);
  
    fetch('http://localhost:3001/upload', {
      method: 'POST',
      body: formData
    })
    .then(response => response.json())
    .then(data => {
      const predictionResult = document.getElementById('predictionResult');
      predictionResult.textContent = 'Prediction: ' + data.prediction;
    })

    
    .catch(error => {
      console.error('Error uploading file: ', error);
      alert('Error uploading file. Please try again.');
    });
  }
  