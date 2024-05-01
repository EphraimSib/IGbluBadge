const { exec } = require('child_process');
const http = require('http');
const fs = require('fs');

// Execute the Python script
exec('python3 IGblueBadge.py', 'python3 my_server.py', (error, stdout, stderr) => {
    if (error) {
        console.error(`Error executing Python script: ${error.message}`);
        return;
    }
    console.log(`Python script output: ${stdout}`);
    // Start the server
    startServer();
});

function startServer() {
    const PORT = 8080;

    const server = http.createServer((req, res) => {
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.end('Hello, this is your custom server!\n');
    });

    server.listen(PORT, () => {
        console.log(`Server is running on port ${PORT}`);
    });

    // Log server events to server.log
    server.on('request', (req)  => {
        fs.appendFile('server.log', `${new Date()} - Request: ${req.url}\n`, (err) => {
            if (err) {
                console.error('Error writing to server.log:', err);
            }
        });
    });
}
