import re

client_server_client = """
import socket

HOST = '127.0.0.1'  # The server's IP address
PORT = 4444         # The server's port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    # Connect to the server at the specified IP and port
    server.connect((HOST, PORT))

    # Send data to the server
    server.send(b'example data')
    print('The client sent: example data')

    # Receive data from the server
    data = server.recv(1024)
    print('The server replied with:', str(data, 'utf-8'))
"""

client_server_server = """
import socket

IP = '127.0.0.1'
PORT = 4444

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    # Start the server on the defined IP and port
    server.bind((IP, PORT))

    # Start accepting connections to the server
    server.listen()
    connection, address = server.accept()

    # Wait for a client connection
    with connection:
        
        # Keep checking for data sent by the client
        while True:
            data = connection.recv(1024)
            if not data:
                break
            connection.send(data)
"""

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
		if len(arguments) != 0:
			for index,item in enumerate(keywords):
				block = block.replace(item,arguments[index])
		with open(self.fileName, 'a') as fp:
			fp.write(block)
