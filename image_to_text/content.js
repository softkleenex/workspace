document.addEventListener('dragover', event => event.preventDefault());
document.addEventListener('drop', event => {
  event.preventDefault();
  const file = event.dataTransfer.files[0];
  if (file && file.type.startsWith('image/')) {
    const reader = new FileReader();
    reader.onload = function(e) {
      const imageDataUrl = e.target.result;
      chrome.runtime.sendMessage({ action: "extractText", image: imageDataUrl }, response => {
        alert("Extracted Text: " + response.text);
      });
    };
    reader.readAsDataURL(file);
  }
});
