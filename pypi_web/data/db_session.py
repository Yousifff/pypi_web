
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from pypi_web.data.modelbase import SqlAlchemyBase
import pypi_web.data.__all_models

class DBSession:
    factory = None
    engine = None

    @staticmethod
    def global_init(db_file: str):
        if DBSession.factory:
            return

        if not db_file or not db_file.strip():
            raise Exception("You must specifiy a database file")

        conn_str = 'sqlite:///'+db_file

        print(f'Connecting to db at {conn_str}')

        engine = create_engine(conn_str, echo=False)
        DBSession.engine = engine
        DBSession.factory = sessionmaker(bind=engine)

        SqlAlchemyBase.metadata.create_all(engine)