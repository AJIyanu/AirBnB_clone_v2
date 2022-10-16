#!/usr/bin/python3
"""
This is a new database storage module
"""

import os
from sqlalchemy import create_engine, MetaData


class DBStorage:
    """
    The database class and storage
    """
    __engine = None
    __session = None

    def __init__(self):
        """This initializes the database storage"""
        user = os.getenv("HBNB_MYSQL_USER")
        pswrd = os.getenv("HBNB_MYSQL_PWD")
        db = os.getenv("HBNB_MYSQL_DB")
        host = os.getenv("HBNB_MYSQL_HOST")
        test = os.getenv("HBNB_ENV")
        url = "{}:{}@{}/{}".format(user, pswrd, host, db)
        self.__engine = create_engine("mysql+mysqldb://{}".format(url), pool_pre_ping=True)
        meta = MetaData(bind=self.__engine)
        if test == "test":
            meta.drop_all()

    