import puppeteer from "puppeteer";

const url = process.argv[2];
const timeout = 8000;

(async () => {
    const browser = await puppeteer.launch({
        headless: false,
    });

    const page = await browser.newPage();

    await page.setViewport({
        width: 1200,
        height: 1200,
        deviceScaleFactor: 1,
    });

    setTimeout(async () => {
        await page.screenshot({
            path: "E:/Ai_Systems/pythonwebscraper/image/image.jpg",
            fullPage: true,
        });
    }, timeout - 2500);

    await page.goto(url, {
        waitUntil: "networkidle0",
        timeout: timeout,
    });

    await page.screenshot({
        path: "E:/Ai_Systems/pythonwebscraper/image/image.jpg",
        fullPage: true,
    });

    await browser.close();
})();