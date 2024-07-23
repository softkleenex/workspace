const express = require('express');
const puppeteer = require('puppeteer');
const bodyParser = require('body-parser');
const app = express();
const port = 3000;

app.use(bodyParser.json({ limit: '10mb' }));

app.post('/search-by-image', async (req, res) => {
  const { image } = req.body;
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  
  await page.goto('https://images.google.com/');
  const [fileChooser] = await Promise.all([
    page.waitForFileChooser(),
    page.click('div[aria-label="Search by image"]')
  ]);
  await fileChooser.accept([image]);

  await page.waitForSelector('div[jsname="jytLes"]');
  const textElements = await page.$$eval('div[jsname="jytLes"]', elements => elements.map(el => el.innerText));
  await browser.close();

  res.json({ text: textElements.join('\n') });
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
