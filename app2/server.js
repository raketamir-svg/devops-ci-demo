const http = require('http');

// ПОРТ должен быть 80, чтобы соответствовать Service и Probe.
const PORT = 80; 

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/html');
  // Возвращаем ожидаемый контент
  res.end('<h1>Hello from App2! (Node.js)</h1>'); 
});

server.listen(PORT, () => {
  console.log(`Server running at http://0.0.0.0:${PORT}/`);
});
