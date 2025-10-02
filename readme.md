创建虚拟环境  
py -3 -m venv .venv  

进入虚拟环境  
.venv\Scripts\activate  

安装 flask 框架  
pip install flask  

安装 mysql 扩展  
pip install flask-sqlalchemy pymysql  

安装时间扩展  
pip install tzdata  


桌面版  
pip install flask pywebview pyinstaller  

打包指定静态文件目录  
pyinstaller --noconsole --onefile main.py \
    --add-data "templates;templates" \
    --add-data "static;static"

CREATE DATABASE `db_python`;  

CREATE TABLE `tasks` (  
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,  
  `plan` varchar(255) NOT NULL DEFAULT '',  
  `state` tinyint(3) unsigned NOT NULL DEFAULT 1 COMMENT '0、未完成；1、已完成',  
  `create_time` datetime NOT NULL,  
  `update_time` datetime NOT NULL,  
  `delete_time` datetime DEFAULT NULL,  
  PRIMARY KEY (`id`)  
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4   COLLATE=utf8mb4_general_ci;  


后台启动项目  
sudo nano /etc/systemd/system/todolist.service  

[Unit]  
Description=Flask App - TodoList  
After=network.target  

[Service]  
User=www-data  
Group=www-data  
WorkingDirectory=/var/www/html/todolist  
Environment="PATH=/var/www/html/todolist/.venv/bin"  
ExecStart=/var/www/html/todolist/.venv/bin/python run.py  
Restart=always  

[Install]  
WantedBy=multi-user.target  

刷新 systemd 配置  
sudo systemctl daemon-reload  

启动服务  
sudo systemctl start todolist  

sudo systemctl enable todolist  

查看状态  
sudo systemctl status calendar  

