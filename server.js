// Dependencies
const axios = require('axios');

// Server port
const PORT = 8080;

// Create a basic HTTP server
const server = require('http').createServer((req, res) => {
 res.writeHead(200, {'Content-Type': 'text/plain'});

 // Fetch data from a RESTful API
 axios.get('https://jsonplaceholder.typicode.com/todos/1')
    .then(response => {
      // Output the data to the server response
      res.end(JSON.stringify(response.data));
    })
    .catch(error => {
      // Handle errors
      console.error('Error fetching data:', error);
      res.end('Error fetching data');
    });
});

// Start the server
server.listen(PORT, () => {
 console.log(`Server running on port ${PORT}`);
});