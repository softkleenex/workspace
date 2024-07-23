chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action === "extractText") {
      const imageUrl = message.image;
      fetch('https://api.example.com/ocr', { // OCR API를 호출
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
      return true;  // sendResponse를 비동기로 사용하기 위해 true 반환
    }
  });

  