from dotenv import load_dotenv
load_dotenv()

import os

class BOT:
    TOKEN = os.environ.get("TOKEN", "")

class API:
    HASH = os.environ.get("API_HASH", "")
    ID = int(os.environ.get("API_ID", 0))

class OWNER:
    ID = int(os.environ.get("OWNER", 1773034985))

class CHANNEL:
    ID = int(os.environ.get("CHANNEL_ID", -1002732527335))

class WEB:
    PORT = int(os.environ.get("PORT", 8080))

class DATABASE:
    URI = os.environ.get("DB_URI", "")
    NAME = os.environ.get("DB_NAME", "Cluster0")
