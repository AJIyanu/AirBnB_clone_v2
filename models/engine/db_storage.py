#!/usr/bin/python3
"""
This is a new database storage module
"""


import os

from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from ..amenity import Amenity
from ..base_model import Base, BaseModel
from ..city import City
from ..place import Place
from ..review import Review
from ..state import State
from ..user import User


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
            meta.drop_all(self.__engine)

    def all(self, cls=None):
        """
        This queries the database if none returns all object otherwise
        retutn selected object
        """
        clas = [User, State, City, Amenity, Place, Review, BaseModel]
        sess = self.__session
        if cls is not None:
            result = sess.query(cls).all
        else:
            result = {}
            for mod in clas:
                try:
                    result.update(sess.query(mod).all())
                except Exception:
                    pass
                finally:
                    continue
        objdict = {}
        for clsdb in result:
            key = "{}.{}".format(clsdb.__name__, clsdb.id)
            objdict.update({key: clsdb})
        return (objdict)

    def new(self, obj):
        """add the object to the current database session (self.__session)"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session (self.__session)"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """creates all tablels"""
        connection = self.__engine.connect()
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=connection, expire_on_commit=False)
        self.__session = scoped_session(session)
