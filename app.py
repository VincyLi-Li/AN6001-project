from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # ✅ Flask 自动在 templates/ 目录查找

if __name__ == "__main__":
    app.run(debug=True, port=5001)  # 运行在5001端口
