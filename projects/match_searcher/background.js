chrome.runtime.onInstalled.addListener(() => {
  chrome.contextMenus.create({
    id: "generateUrl",
    title: "Generate URL with dak.gg",
    contexts: ["selection"]
  });
});

chrome.contextMenus.onClicked.addListener((info, tab) => {
  if (info.menuItemId === "generateUrl" && info.selectionText) {
    chrome.storage.sync.get(['searchRule1', 'searchRule2'], function(result) {
      const searchRule1 = result.searchRule1 || '';
      const searchRule2 = result.searchRule2 || '';
      const selectedText = info.selectionText;
      const words = selectedText.split(/\s+/);
      const formattedString = words.map(word => encodeURIComponent(word.trim())).join('+');

      if (searchRule1.trim() !== '') {
        // Open the first rule URL
        const url1 = `${searchRule1}${formattedString}`;
        chrome.tabs.create({ url: url1 });
      }

      if (searchRule2.trim() !== '') {
        // Open the second rule URLs
        words.forEach(word => {
          const formattedWord = encodeURIComponent(word.trim());
          const url2 = `${searchRule2}${formattedWord}`;
          chrome.tabs.create({ url: url2 });
        });
      }
    });
  }
});
