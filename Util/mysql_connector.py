from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from Util.secrets import CredentialManager


class MySQLConnection:
    Base = None
    SessionLocal = None

    def __init__(self, host: str, user: str, password: str, name: str, port: str) -> None:
        self.host = host
        self.user = user
        self.password = password
        self.name = name
        self.port = port
        if not MySQLConnection.Base or not MySQLConnection.SessionLocal:
            sqlalchemy_database_url = (
                'mysql+pymysql://{user}:{password}@{host}:{port}/{schema}'.format(
                    user=self.user,
                    password=self.password,
                    host=host,
                    port=port,
                    schema=name,
                )
            )
            engine = create_engine(sqlalchemy_database_url)
            MySQLConnection.Base = declarative_base()
            MySQLConnection.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        else:
            raise Exception('You cannot create another MySQL connection')

    @staticmethod
    def get_base() -> object:
        if not MySQLConnection.Base:
            credential_manager = CredentialManager.get_credential_manager()
            MySQLConnection(
                credential_manager.DB_HOST,
                credential_manager.DB_USER,
                credential_manager.DB_PASS,
                credential_manager.DB_NAME,
                credential_manager.DB_PORT
            )
        return MySQLConnection.Base

    @staticmethod
    def get_session() -> object:
        if not MySQLConnection.SessionLocal:
            credential_manager = CredentialManager.get_credential_manager()
            MySQLConnection(
                credential_manager.DB_HOST,
                credential_manager.DB_USER,
                credential_manager.DB_PASS,
                credential_manager.DB_NAME,
                credential_manager.DB_PORT
            )
        return MySQLConnection.SessionLocal

    @staticmethod
    def get_db():
        db_object = MySQLConnection.get_session()
        return db_object()
