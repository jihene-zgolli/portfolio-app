import os

APP_NAME = os.environ.get("APP_NAME", "Portfolio Jihene Zgolli")
APP_VERSION = os.environ.get("APP_VERSION", "1.0.0")
APP_ENV = os.environ.get("APP_ENV", "production")
PORT = int(os.environ.get("PORT", 8000))
