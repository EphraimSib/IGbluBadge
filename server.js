const express = require('express');
const axios = require('axios');
const cors = require('cors');

const app = express();
app.use(cors());

const igAPI = 'https://www.instagram.com/accounts/login/ajax/';

app.get('/igbluebadge', async (req, res) => {
 try {
    const response = await axios.get(igAPI);
    const igData = response.data;
    if (igData.status === 'ok') {
      const blueBadgeStatus = igData.authenticated;
      res.json({
        blueBadgeStatus,
      });
    } else {
      throw new Error('An error occurred while retrieving IG data');
    }
 } catch (error) {
    console.error(error);
    res.status(500).json({
      error: 'Internal Server Error',
    });
 }
});

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
 console.log(`Server is running on port ${PORT}`);
});
