class Container:
    def __init__(self):
        self.content = []
        self.owner = None

    def add(self, item):
        for i in self.content:
            if i.id == item.id:
                i.quantity += item.quantity
                break
        else:
            self.content.append(item)
            item.set_container(self)

    def remove(self, item_id, amount):
        for i in self.content:
            if i.id == item_id:
                i.quantity -= amount
                if i.quantity <= 0:
                    del i

    def is_empty(self):
        return len(self.content) == 0

    def get(self):
        return self.content[:]

    def get_owner(self):
        return self.owner

    def set_owner(self, owner):
        self.owner = owner

    def __str__(self):
        txt = f'Owner: {self.owner.id}\n'
        txt += f'Total items: {sum([i.quantity for i in self.content], 0)}\n'
        model = '{0:<14}{1:^10}'
        txt += '\n'.join([model.format(i.name, i.quantity) for i in self.content])
        return txt


item_keys = [
    'id', 'name', 'type', 'rarity',
    'points', 'craft'
]

class ItemBuilder:
    def __init__(self, item_data, **custom):
        '''Base item class creator to initialize
        item before adressing it into a container.

        - item_data: dict with item information
        -- custom: custom optional data'''
        self.raw = item_data
        for key in item_keys:
            setattr(
                self, key,
                custom.get(key, item_data[key])
            )

    def build(self, container, quantity=1):
        return ItemObj(
                self,
                container=container,
                quantity=quantity
        )


class ItemObj:
    def __init__(self, builder, **sp):
        self.raw = builder.raw

        for key in item_keys:
            setattr(self, key, getattr(builder, key))

        self.container = sp.get('container', None)
        self.owner = self.container.get_owner()
        self.quantity = sp.get('quantity', 0)

    def set_container(self, container_obj):
        self.owner = container_obj

