import os

from dotenv import load_dotenv

load_dotenv('.env.local')

DATABASE_URL = os.environ.get('DATABASE_URL')
