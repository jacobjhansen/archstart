class Topic:
    def __init__(self):
        self.subscribers = set() 
    def registerSubscriber(self, subscriber):
        self.subscribers.add(subscriber)
    def unregisterSubscriber(self, subscriber):
        self.subscribers.discard(subscriber)
    def notifySubscribers(self, data):
        for subscriber in self.subscribers:
            subscriber.processData(data)
