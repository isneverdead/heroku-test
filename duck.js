const webdriver = require('selenium-webdriver');
// const chrome = require(selenium-webdriver/chrome);
console.log("masuk ke function")
(async function getduck() {
  // let driver = await new Builder().forBrowser('chrome').build();
  let chromeOptions = await new webdriver.setChromeOptions()
    .setChromeBinaryPath('/app/.apt/usr/bin/google-chrome')
    .headless()
    .addArguments('disable-dev-shm-usage')
    .addArguments('no-sandbox');
    console.log("chrome option done")
  
  let driver = await new webdriver.Builder()
    .forBrowser('chrome')
    .execute('/app/.chromedriver/bin/chromedriver')
    .setChromeOptions(chromeOptions)
    .build();
    console.log("build chrome done")
  try {
    // Navigate to Url
    await driver.get('https://duckduckgo.com');
        console.log("loading done");
        // Get all the elements available with tag name 'p'
        await driver.findElement(By.id('search_form_input_homepage')).sendKeys('Frz_akbar Instagram', Key.ENTER);
        // for(let e of elements) {
        //     console.log(await e.getText());
        // }
    }
    finally {
        console.log("done");
        // await driver.quit();
    }
})();
  


