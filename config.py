import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "22207976"))
API_HASH = getenv("API_HASH", "5c0ad7c48a86afac87630ba28b42560d")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7496441065:AAFJkK2AaWCFKD_7metQlfinL4s-f7iouXs")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Music:Music@cluster0.zlhy5x4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 180))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002154883019"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "6872968794"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", "https://github.com/AnonymousX1025/AnonXMusic", # dont Change this otherwise u get error 🧧
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/DK_X_BOT")
SUPPORT_CHAT = getenv("SUPPORT_GROUP", "https://t.me/DKXBOT_GROUP")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BQFVzIkAYUP0vuDOaJKq2e3oqJQnYMqV91MQ2jUy_xIiNI7CmaXwnvOmwZmFn9JP1Hwtb8ZA7-oqGPIocQ_xhNC3nX5s3dDpHZ4mPQPIffr4yB_Aof8EWmNEEkPwwOm0aV1F9JdbFoWScONU-cqe7YehUhqFWlqZzIse6Hi6EtyvVb4cZw-hA37glyD8mDADePjEzW324sIGy4u5YNgBMGemHRACU-wiq01x0v_KyymX9AEbtyGvj8WmuEK4g-eyCexaWRM6N7ARiOnvA6uW1JuQbcP7sDT4E3RIu6aXISZXOimD1yKPb7LOsThEHN7CzDKX4zaPLhDVoabvK1jjhDCB0TkxXgAAAAG97p90AA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/3f9e4418ae006de242055.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/3f9e4418ae006de242055.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/10b834b75441dff816692.jpg"
STATS_IMG_URL = "https://telegra.ph/file/10b834b75441dff816692.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/10b834b75441dff816692.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/10b834b75441dff816692.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/10b834b75441dff816692.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/10b834b75441dff816692.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/10b834b75441dff816692.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/10b834b75441dff816692.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/10b834b75441dff816692.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/10b834b75441dff816692.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
