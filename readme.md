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