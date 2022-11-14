#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""

if HBNB_TYPE_STORAGE is "db":
    from models.engine.file_storage import FileStorage as Storage
else:
    from models.engine.db_storage import DBStorage as Storage


storage = Storage()
storage.reload()


