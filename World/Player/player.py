class Player:
    def __init__(self, container_obj):
        self.id = 'player'

        self.inventory = container_obj

        self.level = 1
        self.xp = 0

    def get_xp(self, level):
        if level <= 1: return 0
        return ((level-1)/.2)**2

    def get_level(self, xp):
        from math import sqrt
        return round(sqrt(xp) * .2 + 1, 2)

