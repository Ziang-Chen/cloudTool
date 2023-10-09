# Purpose: Event bus implementation


class event:
    def __init__(self, name):
        self.name = name

    def get(self):
        return self.name


class eventBus:
    def __init__(self):
        self.table = dict()
        self.subscribers = dict()

    def publish(self, e: event):
        if e.get() in self.table.keys():
            for callback in self.subscribers[e.get()]:
                yield callback
        else:
            return lambda: None

    def subscribe(self, e: event, callback):
        if e.get() in self.subscribers.keys():
            self.subscribers[e.get()].append(callback)
        else:
            self.subscribers[e.get()] = [callback]

    def unsubscribe(self, e: event, callback):
        if e.get() in self.subscribers.keys():
            self.subscribers[e.get()].remove(callback)
