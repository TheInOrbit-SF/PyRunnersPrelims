class MemoryHistory:
    def __init__(self):
        self.history = []

    def add(self, value):
        self.history.append(value)

    def recall_last(self):
        return self.history[-1] if self.history else 0
