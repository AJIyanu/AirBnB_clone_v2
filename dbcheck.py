#!/usr/bin/python3
"""
check my code
"""

from models.engine.db_storage import DBStorage
from models.place import Place
from models.state import State
from models.city import City

db = DBStorage()

#trying to reload all datatable
db.reload()
alltable = db.all()
for one in alltable:
    print("{}".format(one))
print("{}".format(alltable))
