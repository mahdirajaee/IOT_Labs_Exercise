from MyMQTT import * 
import time

class SimpleSubscriber:
    def __init__(self, clientID, port, broker, topic_publish):
        self.client = MyMQTT(clientID, "test.mosquitto.org", 1883, self)
        self.broker = broker 
        self.port = port
        self.topic_publish = topic_publish
        self.simplePublisherClient = MyMQTT(clientID, broker, port,None)

    # def notify(self,topic,payload): 
    #     message_received = json.loads(payload)
    #     print(message_received)

    def startSim(self):
        self.simplePublisherClient.start()
        # self.simpleSubscriberClient.mySubscribe(self.topic_subscribe)

    def stopSim(self):
        # self.simpleSubscriberClient.unsubscribe()
        self.simpleSubscriberClient.stop()

    def publish(self, message_to_publish):
        self.simplePublisherClient.myPublish(self.topic_publish, message_to_publish)
        

if __name__ == '__main__':
    broker = 'mqtt.eclipseprojects.io'
    port = 1883
    clientID = 'matt12345'
    topic = 'IoT/exerciseSimpleTest'
    client_simplePub = SimpleSubscriber(clientID, port, broker, topic)
    client_simplePub.startSim()

    # can be usefull to send messages
    # while True:
    #     time.sleep(5)

    while True: 
        user_input = input('Enter a message to publish: ')
        timeStamp = time.time()
        message_to_send = {"message_to_send": user_input, "timeStamp": timeStamp}
        client_simplePub.publish(message_to_send)