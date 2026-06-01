# Code Structure

The game is coded in Python using OOP for the most of it.
Some data structures use YAML or JSON as well.

It's main structure relies on "Context injection" (or some sort of circular dependency injection), States and Managers

The `Game` class is the "Context"
States are the "screens" of the game
Managers manage States, Data and more


## States

The `States` directory contains every state class organized into files named according to the use of the states in it (eg. `common.py` for frequently used states)

Every state has 2 main methods:
    - `run`: The display and logic of the state
    - `update`: An additional method for extra logic (optional)

States inherit from a base State parent that looks like:

```python
class State:
    def __init__(self, id):
        self.id = id

    def run(self, ctx):
        print(self.id)
        input()

    def update(self, ctx):
        pass
```

(`ctx` has to be present in every State class method parameters)

## Managers

Managers reside in the `Utils/managers.py`

Currently, There are 2 main managers:
    - `StateManager`: Manages states
    - `DataManager`: Manages global data

