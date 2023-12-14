from pymongo import MongoClient
from pymongo.database import Database


class _DBConnection:
    def __init__(self):
        self._client = MongoClient('localhost', 27017)
        self._db = self._client['managerpulse']

    @property
    def db(self) -> Database:
        return self._db

    @property
    def client(self) -> MongoClient:
        return self._client


mongo_db = _DBConnection()
