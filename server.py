from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
# 配置允许所有域名跨域
socketio = SocketIO(app, cors_allowed_origins="*")


@app.route('/')
def index():
    return "Hello, World!"


@socketio.on('connect')
def handle_connect():
    print('客户端已连接')


@socketio.on('disconnect')
def handle_disconnect():
    print('客户端已断开连接')


@socketio.on('message')
def handle_message(message):
    print('收到客户端消息:', message)
    # 向客户端发送消息
    socketio.emit('message', '你好，客户端，我收到你的消息了')


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)