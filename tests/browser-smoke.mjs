import { chromium } from "playwright";

const browser = await chromium.launch({headless:true});
const page = await browser.newPage({viewport:{width:1440,height:900}});
const errors = [];
page.on("pageerror", e => errors.push("pageerror: " + e.message));
page.on("console", m => { if(m.type() === "error") errors.push("console: " + m.text()); });

await page.goto("http://127.0.0.1:4173/", {waitUntil:"networkidle", timeout:120000});
await page.waitForFunction(() => document.querySelector("#status")?.textContent.includes("Python pronto"), null, {timeout:120000});

await page.locator("#editor").fill('print("SMOKE_OK")');
await page.locator("#run").click();
await page.waitForFunction(() => document.querySelector("#out")?.textContent.includes("SMOKE_OK"), null, {timeout:30000});

await page.locator("#editor").fill('await install("numpy")\nimport numpy as np\nprint("NUMPY_OK", np.array([1,2,3]).sum())');
await page.locator("#run").click();
await page.waitForFunction(() => document.querySelector("#out")?.textContent.includes("NUMPY_OK 6"), null, {timeout:120000});

await page.locator("#editor").fill('import pygame\npygame.init()\nprint("PYGAME_OK", pygame.version.ver)\npygame.quit()');
await page.locator("#run").click();
await page.waitForFunction(() => document.querySelector("#gameStatus")?.textContent.includes("Jogo encerrado"), null, {timeout:120000});

if(errors.length) throw new Error(errors.join("\n"));
console.log("Browser smoke: Python, NumPy and Pygame execution OK");
await browser.close();
