const http = require('http');
const { spawn } = require('child_process');

const server = http.createServer((req, res) => {
    // 设置响应头，允许长连接以及表明返回的数据是纯文本格式
    res.writeHead(200, {
        'Content-Type': 'text/plain',
        'Connection': 'keep-alive'
    });

    // 这里假设Python脚本名为test.py，可根据实际情况替换
    const pythonProcess = spawn('python', ['test.py']);

    // 处理Python脚本标准输出，逐行返回给客户端
    pythonProcess.stdout.on('data', (data) => {
        const lines = data.toString().split('\n');
        lines.forEach(line => {
            if (line.trim()) {  // 过滤掉空行
                res.write(line + '\n');
            }
        });
    });
    // 以下代码会先打印 'Before sleep'，然后等待3秒（3000毫秒）后再打印 'After sleep'
console.log('Before sleep');
setTimeout(() => {
    console.log('After sleep');
}, 3000);
res.write('Hello, world!\n');

    // 处理Python脚本标准错误输出，逐行返回给客户端（比如Python脚本报错信息等）
    pythonProcess.stderr.on('data', (data) => {
        const lines = data.toString().split('\n');
        lines.forEach(line => {
            if (line.trim()) {  // 过滤掉空行
                res.write(line + '\n');
            }
        });
    });

    // 当Python脚本执行完毕，关闭与客户端的连接
    pythonProcess.on('close', (code) => {
        res.end();
    });
});

server.listen(8080, () => {
    console.log('Server listening on port 8080');
});