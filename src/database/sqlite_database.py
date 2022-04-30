import sqlite3 as sl
from sqlite3 import Connection


class SqlLiteDataBase:
    def __init__(self):
        self.db_name = None
        self.connection = None

    def connect_db(self, db_name: str):
        self.db_name = db_name
        self.connection = sl.connect(db_name)
        return self
