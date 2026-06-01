import Core.refs as ref

class StateManager:
    def __init__(self, *states):
        self.state_pool = states or []
        self.current = None
        self.queue = []

    def add_state(self, state_obj):
        if state_obj not in self.state_pool:
            self.state_pool.append(state_obj)

    def remove_state(self, state_id):
        for state in self.state_pool:
            if state.id == state_id:
                self.state_pool.remove(state)
                return

    def go_back(self):
        if len(self.queue) >= 2:
            self.queue.pop()
            self.current = self.queue[-1]

    def go_to(self, state_id):
        for state in self.state_pool:
            if state.id == state_id:
                self.current = state
                self.queue.append(state)
                return
        else:
            self.go_to(ref.id_wip)

    def run(self, context):
        self.current.run(context)

    def update(self, context):
        self.current.update(context)


class DataManager:
    def __init__(self):
        self.data = {}

    def add(self, key, value):
        self.data[key] = value

    def remove(self, key):
        if key in self.data.keys():
            del self.data[key]

    def wipe(self):
        self.data = {}

    def get(self, key):
        return self.data.get(key, None)


