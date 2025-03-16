document.addEventListener('DOMContentLoaded', () => {
    const buttonContainer = document.querySelector('div[role="button"]');
    if (buttonContainer) {
      const newButton = document.createElement('button');
      newButton.textContent = 'Generate URL';
      newButton.style.marginLeft = '10px';
      newButton.onclick = () => {
        const extractedText = document.querySelector('div[data-id="result-text"]').innerText;
        const formattedText = encodeURIComponent(extractedText.trim());
        const url = `https://dak.gg/er/multi?q=${formattedText}`;
        window.open(url, '_blank');
      };
      buttonContainer.appendChild(newButton);
    }
  });
  