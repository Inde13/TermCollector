class State:
    def __init__(self, id):
        self.id = id

    def run(self, context):
        print(self.id)
        input()

    def update(self, context):
        pass



