from MyMQTT import * 
import time
import json

class SimpleSubscriber:
    def __init__(self, clientID, port, broker, topic_subscribe):
        self.client = MyMQTT(clientID, broker, port, self)
        self.topic_subscribe = topic_subscribe

    def notify(self, topic, payload): 
        message_received = json.loads(payload)
        print(f"Received on topic {topic}: {message_received}")

    def startSim(self):
        self.client.start()
        self.client.mySubscribe(self.topic_subscribe)

    def stopSim(self):
        self.client.stop()

if __name__ == '__main__':
    broker = 'mqtt.eclipseprojects.io'
    port = 1883
    clientID = 'matt12345_sub'
    topic = 'IoT/exerciseSimpleTest'
    client_simpleSub = SimpleSubscriber(clientID, port, broker, topic)
    client_simpleSub.startSim()

    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        client_simpleSub.stopSim()
        print("\nSubscriber stopped.")
