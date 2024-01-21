import os
from typing import Set
class Config(object):
    LOGGER = True
    ALIVE_NAME = os.environ.get("ALIVE_NAME", "@IQTHON")
    APP_ID = int(os.environ.get("APP_ID", 6))
    API_HASH = os.environ.get("API_HASH") or None
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN") or os.environ.get("TG_BOT_TOKEN_BF_HER", None)
class Production(Config):
    LOGGER = False
class Development(Config):
    LOGGER = True
