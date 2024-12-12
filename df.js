   const WebSocket = require('ws');
   const http = require('http');
   const fs = require('fs')

   // 创建HTTP服务器
   const server = http.createServer((req, res) => {
       res.writeHead(200, {'Content-Type': 'text/plain'});
       res.end('WebSocket server is running');
   });

   // 创建WebSocket服务器并绑定到HTTP服务器
   const wss = new WebSocket.Server({server});

   const handleConnected=(FormData)=>{
   //     run python script while callback is

   }
   const sendResponse=(msg)=>{

   }
   wss.on('connection', (ws) => {
       wss.send(

       )
       ws.on('message', (message) => {
           console.log('Received: %s', message);
           ws.send('You sent: ' + message);
       });
       ws.on('close', () => {
           console.log('Client disconnected');
       });
   });

   const handleMessage = (message) => {
       fs.appendFile('data/log/HandleMsgRuntime.log', message + '\n', (err) => {
           console.log(err)
       });
       selectMsg(message);
   };

   const selectMsg = (message) => {
   //     to do

   }


   // 启动服务器
   server.listen(5000, () => {
       console.log('Server started on port 5000');
   });