from rich import inspect, print
import yaml

from Core.managers import StateManager, DataManager
import Core.refs as ref
from States.base import State
from States.common import *
from Utils.display import clr
from World.Items.items import Container, ItemBuilder, ItemObj
from World.Player.player import Player


# Load the whole item 'database'

with open('World/Items/itemdb.yml', 'r') as f:
    item_data = yaml.safe_load(f)

# Main Game class

class Game:
    def __init__(self):
        # States

        self.sm = StateManager(
            Start(), Menu(), Inventory(), WIP(), ItemList()
        )
        self.dm = DataManager()

        self.sm.go_to(ref.id_start_menu)

        # Game stuff

        self.items = [ItemBuilder(i) for i in item_data.values()]
        self.player = Player(Container())

        self.running = True

    def end(self):
        self.running = False

    def run(self):
        # Main game loop

        while self.running:
            clr()
            try:
                self.sm.run(self)
                self.sm.update(self)
            except KeyboardInterrupt:
                break


Game().run()
clr()
print("-Game Closed-")

