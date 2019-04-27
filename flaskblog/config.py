import os

class Config:
    SECRET_KEY = 'b21f90fdcd2db419e7883c49949f58fb'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME='saudababs00@gmail.com'
    MAIL_PASSWORD='Her4631!'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://student:1234@localhost/writerly'


class DevConfig(Config):
    '''
    Class that holds configurations in development mode
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://student:1234@localhost/writerly'
    debug = True

class ProdConfig(Config):
    '''
    '''
    pass

    # SQLALCHEMY_DATABASE_URI =os.environ.get('DATABASE_URL')

config_options = {
'development':DevConfig,
'production':ProdConfig
}
