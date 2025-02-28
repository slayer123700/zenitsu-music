import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters
load_dotenv()


API_ID = 22317880

API_HASH = "5e341628f7176989bcffb2b8fc22445f"

BOT_TOKEN = "7656219426:AAF5748P2BNbK250vSii7XE9VNxSD_ThDq0"

BOT_ID = 7656219426

BOT_USERNAME = "suzune_probot"

OWNER_USERNAME = "SLAYER1237"

BOT_NAME = "Suzune"

ASSUSERNAME = "KHWAISH_HOON"


MONGO_DB_URI = "mongodb+srv://musicbotxd:musicbotxd@cluster0.6thyk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DURATION_LIMIT_MIN = 500000

LOGGER_ID = -1002392274240

DISASTER_LOG = -1002392274240

OWNER_ID = 6018803920

SPECIAL_USER = 5268691896

HEROKU_APP_NAME = None

HEROKU_API_KEY = None

UPSTREAM_REPO = ""

UPSTREAM_BRANCH = "master"

GIT_TOKEN = ""


SUPPORT_CHANNEL = ""

SUPPORT_CHAT = ""

AUTO_LEAVING_ASSISTANT = False
AUTO_LEAVE_ASSISTANT_TIME = 9000


SPOTIFY_CLIENT_ID = "22b6125bfe224587b722d6815002db2b"

SPOTIFY_CLIENT_SECRET = "c9c63c6fbf2f467c8bc68624851e9773"

PLAYLIST_FETCH_LIMIT = 25

TG_AUDIO_FILESIZE_LIMIT = 2147483648
TG_VIDEO_FILESIZE_LIMIT = 2147483648

SONG_DOWNLOAD_DURATION = 9999999
SONG_DOWNLOAD_DURATION_LIMIT = 9999999

TG_AUDIO_FILESIZE_LIMIT = 2147483648
TG_VIDEO_FILESIZE_LIMIT = 2147483648

STRING1 = ""
STRING2 = None 
STRING3 = None 
STRING4 = None
STRING5 = None
STRING6 = None
STRING7 = None


filter = filters.user()
BANNED_USERS = filter
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

START_IMG_URL =  "https://i.ibb.co/yBHkSHZ/photo-2024-12-20-12-20-16-7450467828362117124.jpg"
PLAYLIST_IMG_URL = "https://i.ibb.co/XFyfNRC/photo-2024-12-14-04-11-48-7448115436119392264.jpg"
STATS_IMG_URL = "https://i.ibb.co/THd3s2g/photo-2024-12-14-04-12-49-7448115698112397328.jpg"
TELEGRAM_AUDIO_URL = "https://i.ibb.co/TrJhtN4/photo-2024-12-14-04-12-15-7448115547788542008.jpg"
TELEGRAM_VIDEO_URL = "https://i.ibb.co/XFyfNRC/photo-2024-12-14-04-11-48-7448115436119392264.jpg"
STREAM_IMG_URL = "https://i.ibb.co/THd3s2g/photo-2024-12-14-04-12-49-7448115698112397328.jpg"
SOUNCLOUD_IMG_URL = "https://i.ibb.co/TrJhtN4/photo-2024-12-14-04-12-15-7448115547788542008.jpg"
YOUTUBE_IMG_URL = "https://i.ibb.co/THd3s2g/photo-2024-12-14-04-12-49-7448115698112397328.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://i.ibb.co/XFyfNRC/photo-2024-12-14-04-11-48-7448115436119392264.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://i.ibb.co/THd3s2g/photo-2024-12-14-04-12-49-7448115698112397328.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://i.ibb.co/THd3s2g/photo-2024-12-14-04-12-49-7448115698112397328.jpg"

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
