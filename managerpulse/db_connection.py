from pymongo import MongoClient
from pymongo.database import Database


from .environment import Environment


class _DBConnection:
    def __init__(self):
        self._client = MongoClient(
            Environment.get_instance.ME_CONFIG_MONGODB_URL
        )
        self._db = self._client['managerpulse']

    @property
    def db(self) -> Database:
        return self._db

    @property
    def client(self) -> MongoClient:
        return self._client


mongo_db = _DBConnection()
