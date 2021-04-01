class Publisher:
    def __init__(self):
        self.topics = set()
    def registerTopic(self, topic):
        self.topics.add(topic)
    def unregisterTopic(self, topic):
        self.topics.discard(topic)
    def publishData(self, data):
        for topic in self.topics:
            topic.notifySubscribers(data)