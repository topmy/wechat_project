#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: local.py
@time: 16-3-10 下午5:10
"""


import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__)+'/../')

# sqlite 数据库配置
# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'db/flask.db')

# mysql 数据库配置
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'passwd': '123456',
    'db': 'wechat',
    'port': 3306
}
SQLALCHEMY_DATABASE_URI = \
    'mysql+mysqldb://%s:%s@%s:%s/%s?charset=utf8' % \
    (DB_CONFIG['user'], DB_CONFIG['passwd'], DB_CONFIG['host'], DB_CONFIG['port'], DB_CONFIG['db'])

SQLALCHEMY_POOL_SIZE = 5  # 默认 pool_size=5
SQLALCHEMY_TRACK_MODIFICATIONS = False

CSRF_ENABLED = True
SECRET_KEY = '\x03\xabjR\xbbg\x82\x0b{\x96f\xca\xa8\xbdM\xb0x\xdbK%\xf2\x07\r\x8c'

# 文件上传配置
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'app/static/uploads/')
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
MAX_CONTENT_LENGTH = 2.6 * 1024 * 1024  # 2.6M

# 本地调试邮箱配置
# $ sudo python -m smtpd -n -c DebuggingServer localhost:25
MAIL_SERVER = 'localhost',
MAIL_PORT = 25,
MAIL_USERNAME = None,
MAIL_PASSWORD = None,
MAIL_DEFAULT_SENDER = ('no-reply', 'no-reply@localhost')

# 开发环境邮箱配置
# MAIL_SERVER = 'smtp.163.com',
# MAIL_PORT = 25,
# MAIL_USERNAME = 'xxxxxx@163.com',
# MAIL_PASSWORD = 'xxxxxx',
# MAIL_DEFAULT_SENDER = (u'系统邮箱', 'zhang_he06@163.com')

# 后台管理人员邮件列表
ADMINS = ['455091702@qq.com']


# 微信公众平台配置
APPID = 'wx1cf9245f9f2cc40e'
APPSECRET = 'd4624c36b6795d1d99dcf0547af5443d'

# sendcloud 邮件发送平台
SENDCLOUD_API_USER = 'zhang_he_test_w6kIMK'
SENDCLOUD_API_KEY = 'eZeC3Qwciv4o0lDH'

# qiniu 云存储
QINIU_ACCESS_KEY = 'i3Zi_VQOoeuMDnYkksWvn6TKa0_2C9Wb2NXMtrdn'
QINIU_SECRET_KEY = 'B_0pOtxxaQX8aPqqdMqX2A5v0R99KYKgod5vbkXf'
QINIU_BUCKET_NAME = 'zhendi-open'                       # 七牛空间名称
QINIU_BUCKET_DOMAIN = '7xtmj9.com2.z0.glb.clouddn.com'  # 七牛空间对应域名

# 第三方开放授权登陆

GITHUB_OAUTH = {
    'consumer_key': '0ccd9367a1f81288b127',
    'consumer_secret': '711b6afcc938d760e9e57215dfbdcb115150ddc6',
    'request_token_params': {'scope': 'user:email'},
    'base_url': 'https://api.github.com/',
    'request_token_url': None,
    'access_token_method': 'POST',
    'access_token_url': 'https://github.com/login/oauth/access_token',
    'authorize_url': 'https://github.com/login/oauth/authorize'
}

QQ_OAUTH = {
    'consumer_key': '101187283',  # QQ_APP_ID
    'consumer_secret': '993983549da49e384d03adfead8b2489',  # QQ_APP_KEY
    'base_url': 'https://graph.qq.com',
    'request_token_url': None,
    'request_token_params': {'scope': 'get_user_info'},
    'access_token_url': '/oauth2.0/token',
    'authorize_url': '/oauth2.0/authorize',
}

WEIBO_OAUTH = {
    'consumer_key': '909122383',
    'consumer_secret': '2cdc60e5e9e14398c1cbdf309f2ebd3a',
    'request_token_params': {'scope': 'email,statuses_to_me_read'},
    'base_url': 'https://api.weibo.com/2/',
    'authorize_url': 'https://api.weibo.com/oauth2/authorize',
    'request_token_url': None,
    'access_token_method': 'POST',
    'access_token_url': 'https://api.weibo.com/oauth2/access_token',
    # since weibo's response is a shit, we need to force parse the content
    'content_type': 'application/json',
}


# 日志参数配置
LOG_CONFIG = {
    'version': 1,
    'formatters': {
        'simple': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
        'detail': {
            'format': '%(asctime)s - %(name)s - File: %(filename)s - line: %(lineno)d - %(funcName)s() - %(levelname)s - %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'level': 'INFO'
        },
        'file_app': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'detail',
            'level': 'DEBUG',
            'when': 'D',
            'filename': BASE_DIR + '/log/app.log'
        },
        'file_db': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'detail',
            'level': 'DEBUG',
            'when': 'D',
            'filename': BASE_DIR + '/log/db.log'
        }
    },
    'loggers': {
        'app': {
            'handlers': ['console', 'file_app'],
            'level': 'DEBUG'
        },
        'db': {
            'handlers': ['file_db'],
            'level': 'DEBUG'
        }
    }
}


if __name__ == '__main__':
    import os
    import binascii

    sk = os.urandom(24)
    print sk
    print binascii.b2a_hex(sk)
    print BASE_DIR
    print UPLOAD_FOLDER
    print SQLALCHEMY_DATABASE_URI
