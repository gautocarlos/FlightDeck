import os.path
import re

FRAMEWORK_PATH = os.path.dirname(os.path.dirname(__file__)) +'/'

ADMINS = (
   # ('Your Name', 'your_email@domain.com'),
)

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = os.path.join(FRAMEWORK_PATH,'dev.db')             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
MEDIA_ROOT = ''
MEDIA_URL = ''
SECRET_KEY = '_878&mu1t!-d*u^*@l$afwe$p4r(=*$kyyjy37ibf9t8li5#lv'

DEBUG = False

#MEDIA_ROOT =  os.path.join(FRAMEWORK_PATH, '/flightdeck/media/')
ADMIN_MEDIA_ROOT = os.path.join(FRAMEWORK_PATH, 'flightdeck/adminmedia/')
#MEDIA_URL = '/sitemedia/'
#MEDIA_SERVER = ''
#ADMIN_MEDIA_PREFIX = ''.join([MEDIA_SERVER,'/adminmedia/'])