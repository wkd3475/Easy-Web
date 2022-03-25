const http = require('http');
const fs =require('fs');

http.createServer((req, res) => {
    fs.readFile('./main.html', (err, html) => {
        res.writeHead(200, {"Content-Type": "text/html;charset=UTF-8"});
        res.write(html);
        res.end();
    })
}).listen(8080);