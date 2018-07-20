import os


class Config:
    SECRET_KEY = '5891628bb0b13ce0c676dfde280ba245'  # os.environ.get('SECRET')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # os.environ.get('DB_URI')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('USER')
    MAIL_PASSWORD = os.environ.get('PASS')
