import paho.mqtt.client as PahoMQTT 
import time 
import json 

class MyPublisher: 
    def __init__(self, clientID, port, broker, topic_publish): 
        self.clientID = clientID 
        self.broker = broker 
        self.port = port 
        self.topic_publish = topic_publish
        self.publisherClient = PahoMQTT(clientID, broker, port, None) 

    def startSim(self):
        self.publisherClient.start()

    def stopSim(self):
        self.publisherClient.stop() 

    def publish(self, message_to_publish): 
        self.publisher