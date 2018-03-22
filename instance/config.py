"""Configurations for various stages."""
import os


class Config(object):
    """Parent configuration class."""

    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
    MONGO_URI = os.getenv('MONGODB_URI')
    MONGO_DBNAME = os.getenv('MONGO_DBNAME')


class DevelopmentConfig(Config):
    """Configurations for Development."""

    DEBUG = True


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""

    TESTING = True
    MONGO_URI = os.getenv('MONGO_URI_TEST')
    DEBUG = True


class StagingConfig(Config):
    """Configurations for Staging."""

    DEBUG = True


class ProductionConfig(Config):
    """Configurations for Production."""

    DEBUG = False
    TESTING = False

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}
