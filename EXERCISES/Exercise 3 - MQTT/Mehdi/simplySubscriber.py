from MyMQTT import MyMQTT
import time
import json

class SimpleSubscriber:
    def __init__(self, clientID, broker, port, topic_subscribe):
        self.clientID = clientID
        self.broker = broker
        self.port = port
        self.topic_subscribe = topic_subscribe
        self.simpleSubscriberClient = MyMQTT(clientID, broker, port, self)

    def notify(self, topic, payload):
        message_received = json.loads(payload)
        print(f"Received message on topic {topic}: {message_received}")

    def startSim(self):
        self.simpleSubscriberClient.start()
        self.simpleSubscriberClient.mySubscribe(self.topic_subscribe)

    def stopSim(self):
        self.simpleSubscriberClient.unsubscribe(self.topic_subscribe)
        self.simpleSubscriberClient.stop()

if __name__ == '__main__':
    broker = 'mqtt.eclipseprojects.io'
    port = 1883
    clientID = 'matt12345'
    topic = 'IoT/exerciseSimpleTest'
    client_simpleSub = SimpleSubscriber(clientID, broker, port, topic)
    client_simpleSub.startSim()

    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        print("Stopping the subscriber...")
        client_simpleSub.stopSim()