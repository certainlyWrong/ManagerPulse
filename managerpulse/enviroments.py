import os
from dotenv import load_dotenv


class Enviroments:

    instance = None

    def __init__(self):
        load_dotenv()

        self.MODE = os.getenv('MODE', 'production')
        self.MONGO_INITDB_ROOT_USERNAME = (
            'root'
            if self.MODE == 'development' else os.getenv(
                'MONGO_INITDB_ROOT_USERNAME',
                'root'
            )
        )
        self.MONGO_INITDB_ROOT_PASSWORD = (
            '123456'
            if self.MODE == 'development' else os.getenv(
                'MONGO_INITDB_ROOT_PASSWORD'
            )
        )
        self.ME_CONFIG_MONGODB_ADMINUSERNAME = (
            'root'
            if self.MODE == 'development' else os.getenv(
                'ME_CONFIG_MONGODB_ADMINUSERNAME',
                'root'
            )
        )
        self.ME_CONFIG_MONGODB_ADMINPASSWORD = (
            '123456'
            if self.MODE == 'development' else os.getenv(
                'ME_CONFIG_MONGODB_ADMINPASSWORD'
            )
        )

        self.mongo_connection_url = (
            f"mongodb://{self.MONGO_INITDB_ROOT_USERNAME}:"
            f"{self.MONGO_INITDB_ROOT_PASSWORD}@mongo:27017"
        )

        self.ME_CONFIG_MONGODB_URL = (
            self.mongo_connection_url
            if self.MODE == 'development' else os.getenv(
                'ME_CONFIG_MONGODB_URL',
                self.mongo_connection_url
            )
        )

        self.CLIENT_SERVICE_URL = os.getenv(
            'CLIENT_SERVICE_URL',
            'http://clientpulse:3000/api/v1/client/'
        )

        self.PRODUCT_SERVICE_URL = os.getenv(
            'PRODUCT_SERVICE_URL',
            'http://productpulse:8000/api/v1/product/'
        )

        self.MONGO_HOST = (
            'localhost' if self.MODE == 'development' else 'localhost'
        )

        self.MONGO_PORT = 27017

    def __str__(self) -> str:
        return (
            f"MODE: {self.MODE}\n"
            f"MONGO_INITDB_ROOT_USERNAME: {self.MONGO_INITDB_ROOT_USERNAME}\n"
            f"MONGO_INITDB_ROOT_PASSWORD: {self.MONGO_INITDB_ROOT_PASSWORD}\n"
            f"ME_CONFIG_MONGODB_ADMINUSERNAME: "
            "{self.ME_CONFIG_MONGODB_ADMINUSERNAME}\n"
            f"ME_CONFIG_MONGODB_ADMINPASSWORD: "
            "{self.ME_CONFIG_MONGODB_ADMINPASSWORD}\n"
            f"ME_CONFIG_MONGODB_URL: {self.ME_CONFIG_MONGODB_URL}\n"
            f"CLIENT_SERVICE_URL: {self.CLIENT_SERVICE_URL}\n"
            f"PRODUCT_SERVICE_URL: {self.PRODUCT_SERVICE_URL}\n"
            f"MONGO_HOST: {self.MONGO_HOST}\n"
            f"MONGO_PORT: {self.MONGO_PORT}\n"
        )

    @classmethod
    @property
    def get_instance(cls) -> 'Enviroments':
        if cls.instance is None:
            cls.instance = Enviroments()
        print(cls.instance)
        return cls.instance
