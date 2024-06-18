const http = require('http');

const port = process.argv[2];



http.createServer((req, res) => {

    // Add your Selenium code here

    

    const {Builder, By, Key, until} = require('selenium-webdriver');



(async function example() {

 let driver = await new Builder().forBrowser('chrome').build();

 try {

    await driver.get('https://www.instagram.com/');

    await driver.findElement(By.name('username')).sendKeys('your-username');

    await driver.findElement(By.name('password')).sendKeys('your-password');

    await driver.findElement(By.css('button[type="submit"]')).click();

    await driver.wait(until.urlIs('https://www.instagram.com/'), 5000);

    await driver.quit();

 } catch (error) {

    console.log(error);

 }

})();

    

    res.writeHead(200, {'Content-Type': 'text/html'});

    res.end('Hello World!');

}).listen(port);



console.log(`Server running at http://localhost:${port}/`)