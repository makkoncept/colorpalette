import os


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "N6q067SQG7894Yw28d85BqWu4"
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024  # image size upload limit (2 MB)
