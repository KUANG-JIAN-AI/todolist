class Config:
    SECRET_KEY = 'you-will-never-guess'
    # SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:@127.0.0.1:3306/db_python'
    # 如果你用 pymysql:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@127.0.0.1:3306/db_python'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
