from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def index():
    # 直接返回同一目录下的 index.html 文件
    return send_file('index.html')

if __name__ == '__main__':
    # 启动 Flask 服务器，调试模式下可自动重启
    app.run(debug=True, host='0.0.0.0', port=5000)
