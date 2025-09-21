from threading import Thread
import webview
from app import app   # 这里导入你原来的 Flask 实例（比如 app.py 里定义的 app）

def run_flask():
    # 启动 Flask 服务（关闭 debug，避免多次启动）
    app.run(host="127.0.0.1", port=5000, debug=True, use_reloader=False)

if __name__ == "__main__":
    # 后台线程运行 Flask
    t = Thread(target=run_flask, daemon=True)
    t.start()

    # 桌面窗口加载 Flask 页面
    webview.create_window("TodoList 应用", "http://127.0.0.1:5000", width=800, height=700)
    webview.start()
