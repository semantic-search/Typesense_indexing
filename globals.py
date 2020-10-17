import os
from dotenv import load_dotenv
load_dotenv()
MONGO_HOST = os.getenv("MONGO_HOST")
DB = os.getenv('MONGO_DB')
PORT = os.getenv('MONGO_PORT')
MONGO_USER = os.getenv('MONGO_USER')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD')

REDIS_HOSTNAME = os.getenv("REDIS_HOSTNAME")
REDIS_PORT = os.getenv("REDIS_PORT")
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")
REDIS_DB = '0'

TYPESENSE_HOST=os.getenv('TYPESENSE_HOST')
TYPESENSE_PORT=os.getenv('TYPESENSE_PORT')
TYPESENSE_API_KEY=os.getenv('TYPESENSE_API_KEY')
COLLECTION_NAME="files_cache"