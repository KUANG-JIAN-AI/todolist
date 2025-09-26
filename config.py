class Config:
    SECRET_KEY = 'kyou-ken'
    # 如果你用 pymysql:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@127.0.0.1:3306/db_python'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
