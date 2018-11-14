import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'abadsecretkey'
    MAX_CONTENT_LENGTH = 1 * 1024 * 1024     # image size upload limit (4 MB)
