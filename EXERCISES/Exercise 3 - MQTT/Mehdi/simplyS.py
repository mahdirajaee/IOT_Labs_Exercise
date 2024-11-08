from MyMQTT import * 
import time

class SimpleSubscriber:
    def __init__(self, clientID, port, broker, topic_subscribe):
        self.client = MyMQTT(clientID, "test.mosquitto.org", 1883, self)
        self.broker = broker 
        self.port = port
        self.topic_subscribe = topic_subscribe
        self.simpleSubscriberClient = MyMQTT(clientID, broker, port)

    def notify(self,topic,payload): 
        message_received = json.loads(payload)
        print(message_received)

    def startSim(self):
        self.simpleSubscriberClient.start()
        self.simpleSubscriberClient.mySubscribe(self.topic_subscribe)

    def stopSim(self):
        self.simpleSubscriberClient.unsubscribe()
        self.simpleSubscriberClient.stop()

if __name__ == '__main__':
    broker = 'mqtt.eclipseprojects.io'
    port = 1883
    clientID = 'matt12345'
    topic = 'IoT/exerciseSimpleTest'
    client_simpleSub = SimpleSubscriber(clientID, port, broker, topic)
    client_simpleSub.startSim()
    while True:
        time.sleep(5)
