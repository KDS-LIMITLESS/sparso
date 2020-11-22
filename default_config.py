import os
from datetime import timedelta

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///site'
SQLALCHEMY_TRACK_MODIFICATIONS = False
JWT_SECRET_KEY = os.environ["JWT_SECRET_KEY"]
JWT_ERROR_MESSAGE_KEY = "Error"
JWT_BLACKLIST_ENABLED = True
JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=1)
JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=5)
