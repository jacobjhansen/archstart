from subscriber_template import Subscriber
from topic_template import Topic
from publisher_template import Publisher

# Initialize publishers
PUB = Publisher()

# Initialize topics
TOPIC = Topic()

# Initialize subscribers
SUB = Subscriber()

# Register topics to publishers
PUB.registerTopic(TOPIC)

# Register subscribers to topics
TOPIC.registerSubscriber(SUB)

# Publish data
PUB.publishData('data')