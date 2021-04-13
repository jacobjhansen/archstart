import re
main_subroutine_main = """
def main():
    # Main function calls subroutines here
    SUBROUTINE("arg")

if __name__ == "__main__":
    main()
"""

main_subroutine_sub = """
def SUBROUTINE(arg):
    # Subroutine logic goes here
    return arg
"""

pub_sub_pub = """
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
"""

pub_sub_sub = """
class Subscriber:
    def processData(self, data):
        print(data)
"""

pub_sub_topic = """
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
"""

pub_sub_driver = """
# Register topics to publishers
PUB.registerTopic(TOPIC)

# Register subscribers to topics
TOPIC.registerSubscriber(SUB)

# Publish data
PUB.publishData('data')
"""


class FileCreation:
	def __init__(self, fileName):
		self.fileName = fileName
		self.createFile()

	def createFile(self):
		# Creates a new file
		with open(self.fileName, 'w') as fp:
			fp.write('')
	
	def addSection(self,block,arguments):
		keywords = filter(None, [x.strip() for x in re.findall(r"\b[A-Z\s]+\b", block)])
		for index,item in enumerate(keywords):
			block = block.replace(item,arguments[index])
		with open(self.fileName, 'a') as fp:
			fp.write(block)
