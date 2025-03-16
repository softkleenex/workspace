document.addEventListener('DOMContentLoaded', function() {
    // Load stored search rules
    chrome.storage.sync.get(['searchRule1', 'searchRule2'], function(result) {
        if (result.searchRule1) {
            document.getElementById('searchRule1').value = result.searchRule1;
        }
        if (result.searchRule2) {
            document.getElementById('searchRule2').value = result.searchRule2;
        }
    });

    document.getElementById('generateUrl').addEventListener('click', generateUrls);
    document.getElementById('inputString').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            generateUrls();
        }
    });

    function generateUrls() {
        const inputString = document.getElementById('inputString').value;
        const searchRule1 = document.getElementById('searchRule1').value;
        const searchRule2 = document.getElementById('searchRule2').value;
        const words = inputString.split(/\s+/);
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
    }

    document.getElementById('lensSearch').addEventListener('click', function() {
        const lensUrl = 'https://lens.google.com/search?ep=cntpubb&hl=ko-KR&re=df&s=4&p=AbrfA8qxs13PPthzWLH6NCsDdEr1PMit87Qi_xepBrHlDGhMSlmKMPuUoolo3ReUIAtreOuBjuCmH09UlFEYkQ9aIJLSKUFJVpVrxa5e_lArkYUkCfQCVSVaRLfuw3Bw2Yv6e3MuUbq_p8MZ_8svM75QgktIgNIgvrqnD0ia6s2K0-D1kE-8678Jhv1zz7AxnNJAKcF8mxbBUrleBTwDRCj78c8At4iD8erS5J7SHlpnUmibh69xwSmW3Q7m4Ik8a1eO7HKbpLcAbDt33fAUv3hYpyeoUm9toFBw3-9FERhBalCiiztrOQ%3D%3D#lns=W251bGwsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLG51bGwsIkVrY0tKRFppTnpCa00yRXpMVEZqWVdVdE5ERTNNeTFoWVdFM0xXWmxNRGRqTUdRNU9UUmxaaElmT0hoMmJsZGFTRlJpWlRCYWMwWldkMUYzZG5veE4waFhNekJtTTBSU2F3PT0iLG51bGwsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLG51bGwsWyI0Nzc5N2NjNi1iZGJhLTRkN2YtOWI2Mi0yNjQ2MTQ1YzEzNDEiXV0=';
        chrome.tabs.create({ url: lensUrl });
    });

    document.querySelector('.toggle-btn').addEventListener('click', function() {
        const extraContent = document.querySelector('.extra-content');
        if (extraContent.classList.contains('visible')) {
            extraContent.classList.remove('visible');
            this.innerHTML = '&#9660;';
        } else {
            extraContent.classList.add('visible');
            this.innerHTML = '&#9650;';
        }
    });

    document.getElementById('searchRule1').addEventListener('input', function() {
        // Save search rule 1
        const searchRule1 = document.getElementById('searchRule1').value;
        chrome.storage.sync.set({ searchRule1: searchRule1 });
    });

    document.getElementById('searchRule2').addEventListener('input', function() {
        // Save search rule 2
        const searchRule2 = document.getElementById('searchRule2').value;
        chrome.storage.sync.set({ searchRule2: searchRule2 });
    });
});
