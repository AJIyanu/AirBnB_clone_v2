#!/usr/bin/python3
"""
check my code
"""

from models.engine.file_storage import FileStorage
from models.place import Place
from models.state import State
from models.city import City

fs = FileStorage()

"""
# All States
all_states = fs.all(Place)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

print(all_states)

# Create a new State
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
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])
"""

# create state
state = State()
city = City()
city1 = City()
city2 = City()
state.name = "AJ"
city.name = "Iyanu"
city.state_id = state.id
city1.state_id = state.id
city2.state_id = state.id
fs.new(state)
fs.new(city)
fs.new(city1)
fs.new(city2)
fs.save()
print("This state is: {}".format(state))
print("This is city: {}".format(city))
print()
print(fs.all())
print()
print(state.cities)
fs.delete(state)
fs.delete(city)
fs.delete(city1)
fs.delete(city2)
