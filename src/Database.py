import sqlalchemy
import pandas as pd


class DataBase():
    def __init__(self):
        host = "host"
        user = "user"
        password = "password"
        database = "database"
        self.engine = self.connect(user, password, database, host)
    def __del__(self):
        print("Close database connection.")

    def execute(self, query, args={}):
        try:
            return pd.read_sql(query, self.engine)
        except Exception:
            return

    def make_url(self, user, password, host, port, db):
        url = 'postgresql://{}:{}@{}:{}/{}'
        url = url.format(user, password, host, port, db)
        return url

    def connect(self, user, password, db, host, port=5432):
        url = self.make_url(user, password, host, port, db)
        engine = sqlalchemy.create_engine(url, client_encoding='utf8')
        return engine
