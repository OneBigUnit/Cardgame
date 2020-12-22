import os


class Config:
    SECRET_KEY = "\xc4\xcc#\xe0\xce`}S\x85\xc42\x94\xfe\xff2{\x14n&y+\xbf\xc6u"
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "cardgame.noreply@gmail.com"
    MAIL_PASSWORD = "#CardGameNoReply#"