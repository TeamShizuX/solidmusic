from dotenv import load_dotenv
from os import path, getenv


if path.exists("local.env"):
    load_dotenv("local.env")
else:
    load_dotenv()


class Config:
    API_ID = int(getenv("API_ID", "0"))
    API_HASH = getenv("API_HASH", "abc123")
    BOT_TOKEN = getenv("BOT_TOKEN", "1234:abcd")
    SESSION = getenv("SESSION_NAME", "session")
    OWNER_ID = int(getenv("OWNER_ID", "1952053555"))
    SUPPORT = getenv("GROUP_SUPPORT", "https://t.me/solidprojects_chat")
    CHANNEL = getenv("UPDATES_CHANNEL", "https://t.me/solidprojects")
    UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/TeamShizuX/solidmusic")


config = Config()
