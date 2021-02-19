import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 1234567))

    API_HASH = os.environ.get("API_HASH", "")

    FROM_CHANNEL = os.environ.get("FROM_CHANNEL", "")

    TO_CHANNEL = os.environ.get("TO_CHANNEL", "")