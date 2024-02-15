// frontend/script.js
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
  