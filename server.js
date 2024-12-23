const http = require('http');
const {spawn} = require('child_process');
// log at data/log/Server.log
const logToFile = require('log-to-file');


const logPath= './data/log/Server.log';
const logger = (level,content) => {logToFile(`${level} - ${content}`,  logPath)};

const server = http.createServer((req, res) => {
    const interpreterPath = 'python';
    const entryScript = './main.py'
    function getRequestParams(req)  {
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


    }
    //   http://localhost:3000/stream?12=12&122=1122
    if (req.url.startsWith('/stream')) {
        res.writeHead(200, {
            'Content-Type': 'text/event-stream',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive'
        });
        logger('INFO',`Connected to ${req.url}`);
        const requestParams = getRequestParams(req);
        let paramValue = JSON.stringify(requestParams)
        logger('INFO',`Receive ${paramValue} to ${entryScript}`);
        console.log(interpreterPath)
        const pythonProcess = spawn(interpreterPath, [entryScript, paramValue]);
        pythonProcess.stdout.on('data', (data) => {
        res.write(data);
    });

    pythonProcess.stderr.on('data', (data) => {
        res.write(data);
    });

    pythonProcess.on('close', (code) => {
        res.end();
    });
        // handleConnected(requestParams);
        // res.end()
    } else {
        res.writeHead(404);
        res.end();
    }
});


server.listen(3000, () => {
    console.log('Server is running on http://localhost:3000');
});
