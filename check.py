#!/usr/bin/python3
"""
check my code
"""

from models.engine.file_storage import FileStorage
from models.place import Place
from models.state import State

fs = FileStorage()

# All States
all_states = fs.all(Place)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

print(all_states)

"""# Create a new State
new_state = State()
new_state.name = "California"
fs.new(new_state)
fs.save()
print("New State: {}".format(new_state))
print(type(new_state))
print(fs.all())
fs.delete(new_state)
print(fs.all())

# All States
#all_states = fs.all(State)
#print("All States: {}".format(len(all_states.keys())))
#for state_key in all_states.keys():
#    print(all_states[state_key])
"""
