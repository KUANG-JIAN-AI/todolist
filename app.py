import os
from flask import Flask
from config import Config
from model import db
from router import register_routes

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static"),
)
app.config.from_object(Config)

# 初始化数据库
db.init_app(app)

# 注册路由
register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
