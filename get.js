
const {Builder, By, Key} = require('selenium-webdriver');
(async function example() {
    let driver = await new Builder().forBrowser('chrome').build();
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
  
