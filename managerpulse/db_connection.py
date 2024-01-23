from pymongo import MongoClient
from pymongo.database import Database
import os

MONGO_HOST = os.environ.get('MONGO_HOST', 'localhost')
MONGO_PORT = int(os.environ.get('MONGO_PORT', 27017))
MONGO_USERNAME = os.environ.get('MONGO_INITDB_ROOT_USERNAME', 'root')
MONGO_PASSWORD = os.environ.get('MONGO_INITDB_ROOT_PASSWORD', '123456')


class _DBConnection:
    def __init__(self):
        self._client = MongoClient(
            f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}"
            f"@{MONGO_HOST}:{MONGO_PORT}"
        )
        self._db = self._client['managerpulse']

    @property
    def db(self) -> Database:
        return self._db

    @property
    def client(self) -> MongoClient:
        return self._client


mongo_db = _DBConnection()
