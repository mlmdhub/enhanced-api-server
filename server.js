const http = require('http');
const {PythonShell} = require("python-shell");
const { spawn } = require('child_process');
const server = http.createServer((req, res) => {
    //   http://localhost:3000/stream?12=12&122=1122
    if (req.url.startsWith('/stream')) {
        res.writeHead(200, {
            'Content-Type': 'text/event-stream',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive'
        });
        handleConnected(getRequestParams(req));
        res.end()
    } else {
        res.writeHead(404);
        res.end();
    }
});
const getRequestParams = (req) => {
    const reqParams = req.url.split('?')[1];
    const requestParams = {};
    if (reqParams) {
        const params = reqParams.split('&');
        params.forEach(param => {
            const [key, value] = param.split('=');
            requestParams[key] = value;
        })
    }
    return requestParams;
}
const handleConnected = (requestParams) => {
    let paramValue = JSON.stringify(requestParams)
    console.log(paramValue)

// 使用spawn启动Python脚本，并传递参数
const pythonProcess = spawn('python', ['./main.py', paramValue]);

// 监听Python脚本的标准输出，获取正常执行的结果
pythonProcess.stdout.on('data', (data) => {
    console.log(`Python脚本输出: ${data}`);
});

// 监听Python脚本的标准错误输出，获取报错信息
pythonProcess.stderr.on('data', (data) => {
    console.error(`Python脚本报错: ${data}`);
});

// 监听Python脚本执行结束事件
pythonProcess.on('close', (code) => {
    console.log(`Python脚本退出码: ${code}`);
    if (code!== 0) {
        console.error('Python脚本执行出错');
    }
});
}
server.listen(3000, () => {
    console.log('Server is running on http://localhost:3000');
});
