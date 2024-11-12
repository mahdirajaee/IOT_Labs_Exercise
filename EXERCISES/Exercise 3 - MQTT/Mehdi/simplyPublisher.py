from MyMQTT import MyMQTT
import time
import json

class SimplePublisher:
    def __init__(self, clientID, broker, port, topic_publish):
        self.clientID = clientID
        self.broker = broker
        self.port = port
        self.topic_publish = topic_publish
        self.simplePublisherClient = MyMQTT(clientID, broker, port, None)

    def startSim(self):
        self.simplePublisherClient.start()

    def stopSim(self):
        self.simplePublisherClient.stop()

    def publish(self, message_to_publish):
        self.simplePublisherClient.myPublish(self.topic_publish, json.dumps(message_to_publish))

if __name__ == '__main__':
    broker = 'mqtt.eclipseprojects.io'
    port = 1883
    clientID = 'matt12345'
    topic = 'IoT/exerciseSimpleTest'
    client_simplePub = SimplePublisher(clientID, broker, port, topic)
    client_simplePub.startSim()

    try:
        while True:
            user_input = input('Enter a message to publish: ')
            timeStamp = time.time()
            message_to_send = {"message_to_send": user_input, "timeStamp": timeStamp}
            client_simplePub.publish(message_to_send)
    except KeyboardInterrupt:
        print("Stopping the publisher...")
        client_simplePub.stopSim()