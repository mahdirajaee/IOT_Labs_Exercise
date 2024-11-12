from MyMQTT import * 
import time
import json

class SimplePublisher:
    def __init__(self, clientID, port, broker, topic_publish):
        self.client = MyMQTT(clientID, broker, port, None)
        self.topic_publish = topic_publish

    def startSim(self):
        self.client.start()

    def stopSim(self):
        self.client.stop()

    def publish(self, message_to_publish):
        self.client.myPublish(self.topic_publish, json.dumps(message_to_publish))

if __name__ == '__main__':
    broker = 'mqtt.eclipseprojects.io'
    port = 1883
    clientID = 'matt12345_pub'
    topic = 'IoT/exerciseSimpleTest'
    client_simplePub = SimplePublisher(clientID, port, broker, topic)
    client_simplePub.startSim()

    while True:
        user_input = input('Enter a message to publish: ')
        timeStamp = time.time()
        message_to_send = {"message_to_send": user_input, "timeStamp": timeStamp}
        client_simplePub.publish(message_to_send)
