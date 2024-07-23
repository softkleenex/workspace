chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.action === "extractText") {
    const imageUrl = message.image;
    fetch('http://localhost:3000/search-by-image', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ image: imageUrl })
    })
    .then(response => response.json())
    .then(data => {
      sendResponse({ text: data.text });
    })
    .catch(error => {
      console.error('Error:', error);
      sendResponse({ text: 'Failed to extract text' });
    });
    return true;  // 비동기 sendResponse 사용
  }
});
