class Config:
    SECRET_KEY = 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:@localhost:3306/db_python'
    # 如果你用 pymysql:
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/flaskdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
