const http = require('node:http');

const PORT = 3000;

const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
  res.end(`<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8" />
  <title>Hello AI Coding</title>
</head>
<body>
  <h1>hello ai coding</h1>
</body>
</html>`);
});

server.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
