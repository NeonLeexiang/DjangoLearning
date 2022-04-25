from .common import *


"""
    线上环境和开发环境不同的是，为了安全，DEBUG 模式被关闭，SECRET_KEY 从环境变量获取，ALLOWED_HOSTS 设置了允许的 HTTP HOSTS（具体作用见后面的讲解）。
"""

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []