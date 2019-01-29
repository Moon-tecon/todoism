import os

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class Operations:
    RESET_PASSWORD = 'reset-password'
    CHANGE_EMAIL = 'change-email'
    CONFIRM = 'confirm'


class BaseConfig(object):
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    MAX_CONTENT_LENGTH = 3 * 1024 * 1024

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = ('Admin', MAIL_USERNAME)

    PROJECT_ADMIN_EMAIL = os.getenv('PROJECT_ADMIN', MAIL_USERNAME)
    ADMIN_EMAIL = os.getenv('ADMIN_EMAIL', MAIL_USERNAME)

    DEFAULT_PASSWORD = os.getenv('DEFAULT_PASSWORD')

    USERS_PER_PAGE = 20

    MAIL_SUBJECT_PREFIX = '[泰科论坛]'

    UPLOADS_DEFAULT_DEST = os.path.join(basedir, 'uploads')
    UPLOAD_PATH = os.path.join(UPLOADS_DEFAULT_DEST, 'files')
    TECON_PATH = os.path.join(UPLOADS_DEFAULT_DEST, 'tecon')

    AVATARS_SAVE_PATH = os.path.join(UPLOADS_DEFAULT_DEST, 'avatars')
    AVATARS_SIZE_TUPLE = (30, 60, 150)

    PHOTO_SIZE = {'small': 300}
    PHOTO_SUFFIX = {PHOTO_SIZE['small']: '_s'}  # thumbnail

    SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')

    BOOTSTRAP_SERVE_LOCAL = True

    POST_PER_PAGE = 10
    TOPIC_PER_PAGE = 10
    NOTIFICATION_PER_PAGE = 30
    MAX_REPORT_TIME = os.getenv('MAX_REPORT_TIME')
    SEARCH_RESULT_PER_PAGE = 18
    NEWS_PER_PAGE = 9
    MANAGE_NEWS_PER_PAGE = 20


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-dev.db')


class TestingConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'      # in-memory database


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///' + os.path.join(basedir, 'data.db'))


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
