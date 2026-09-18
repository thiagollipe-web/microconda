import { chromium } from "playwright";

const browser = await chromium.launch({headless:true});
const page = await browser.newPage({viewport:{width:390,height:844}, deviceScaleFactor:1, isMobile:true, hasTouch:true});
const errors = [];
page.on("pageerror", e => errors.push("pageerror: " + e.message));
page.on("console", m => { if(m.type() === "error") errors.push("console: " + m.text()); });

await page.goto("http://127.0.0.1:4173/", {waitUntil:"networkidle", timeout:30000});
await page.waitForFunction(() => document.querySelector("#status")?.textContent.includes("Studio pronto"), {timeout:30000});

const editor = page.locator("#editor");
await editor.fill('<!doctype html><html><body><canvas id="game" width="320" height="180"></canvas><script>const c=document.getElementById("game"),x=c.getContext("2d");x.fillStyle="red";x.fillRect(10,10,30,30);console.log("JS_OK");</script></body></html>');
await page.locator("#run").click();
await page.waitForFunction(() => document.querySelector("#gameStatus")?.textContent.includes("Jogo em execução"), {timeout:10000});

const frame = page.frameLocator("iframe.preview-frame");
await frame.locator("canvas#game").waitFor({state:"visible",timeout:10000});

await page.locator("#stopGame").click();
await page.waitForFunction(() => document.querySelector("#gameStatus")?.textContent.includes("Jogo parado"), {timeout:5000});

await page.locator("#download").click();
await page.waitForTimeout(300);
if(errors.length) throw new Error(errors.join("\n"));
console.log("Browser smoke: mobile editor, preview, touch-capable viewport and export flow OK");
await browser.close();
