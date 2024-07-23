document.getElementById('searchButton').addEventListener('click', () => {
    const fileInput = document.getElementById('upload');
    if (fileInput.files.length === 0) {
      alert("Please select an image first.");
      return;
    }
  
    const file = fileInput.files[0];
    const reader = new FileReader();
    reader.onload = function(event) {
      const imageDataUrl = event.target.result;
      chrome.runtime.sendMessagdocument.getElementById('searchButton').addEventListener('click', () => {
        const fileInput = document.getElementById('upload');
        if (fileInput.files.length === 0) {
          alert("Please select an image first.");
          return;
        }
      
        const file = fileInput.files[0];
        const reader = new FileReader();
        reader.onload = function(event) {
          const imageDataUrl = event.target.result;
          chrome.runtime.sendMessage({ action: "extractText", image: imageDataUrl }, (response) => {
            document.getElementById('result').innerText = response.text;
          });
        };
        reader.readAsDataURL(file
      e({action: "extractText", image: imageDataUrl}, (response) => {
        document.getElementById('result').innerText = response.text;
      });
    };
    reader.readAsDataURL(file);
  });
  