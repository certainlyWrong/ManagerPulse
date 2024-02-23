import os
from dotenv import load_dotenv


class Environment:

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

        self.ME_CONFIG_MONGODB_URL = (
            "mongodb://root:123456@localhost:27017/"
            if self.MODE == 'development' else os.getenv(
                'ME_CONFIG_MONGODB_URL'
            )
        )

        self.CLIENT_SERVICE_URL = os.getenv(
            'CLIENT_SERVICE_URL',
            'http://clientpulse:3000/api/v1/client/'
        )

        self.client_url = self.CLIENT_SERVICE_URL

        self.PRODUCT_SERVICE_URL = os.getenv(
            'PRODUCT_SERVICE_URL',
            'http://productpulse:8000/api/v1/product/'
        )

        self.product_url = self.PRODUCT_SERVICE_URL

    def __str__(self) -> str:
        return (
            f"MODE: {self.MODE}\n"
            f"MONGO_INITDB_ROOT_USERNAME: {self.MONGO_INITDB_ROOT_USERNAME}\n"
            f"MONGO_INITDB_ROOT_PASSWORD: {self.MONGO_INITDB_ROOT_PASSWORD}\n"
            f"ME_CONFIG_MONGODB_ADMINUSERNAME: "
            f"{self.ME_CONFIG_MONGODB_ADMINUSERNAME}\n"
            f"ME_CONFIG_MONGODB_ADMINPASSWORD: "
            f"{self.ME_CONFIG_MONGODB_ADMINPASSWORD}\n"
            f"ME_CONFIG_MONGODB_URL: {self.ME_CONFIG_MONGODB_URL}\n"
            f"CLIENT_SERVICE_URL: {self.CLIENT_SERVICE_URL}\n"
            f"PRODUCT_SERVICE_URL: {self.PRODUCT_SERVICE_URL}\n"
        )

    @classmethod
    @property
    def get_instance(cls) -> 'Environment':
        if cls.instance is None:
            cls.instance = Environment()
        print(cls.instance)
        return cls.instance
