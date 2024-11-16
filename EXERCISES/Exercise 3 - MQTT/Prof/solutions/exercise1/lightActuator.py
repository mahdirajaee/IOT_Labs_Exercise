from MyMQTT import *
import time

class LightActuator:
    def __init__(self,clientID,broker,port,topic_subscribe):
        self.lightStatus = "OFF"
        self.lightClientSub = MyMQTT(clientID,broker,port,self)
        self.topic_subscribe = topic_subscribe
    
    # this is the part where he asks for the exam to be consdiered  when you want to recerive the message when want to perform somehthing 
    def notify(self,topic,payload):
        message_json = json.loads(payload)
        self.lightStatus = message_json["status"]
        if self.lightStatus == 1:
            #send status because the light is the same as the status
            # if ... 
            print (f'The Light was turned ON at {time.ctime(message_json["timestamp"])}')
        else:
            print (f'The Light was turned OFF at {time.ctime(message_json["timestamp"])}')
            
    def startSim(self):
        self.lightClientSub.start()
        self.lightClientSub.mySubscribe(self.topic_subscribe)
    
    def stopSim(self):
        self.lightClientSub.unsubscribe()
        self.lightClientSub.stop()

if __name__ == "__main__":
    clientID = "rafafontana12131997"
    broker = "mqtt.eclipseprojects.io"
    port = 1883
    #topic to subscribe
    topic_subscribe_lA = "IoT/rafafontana1234/led/set"
    lightSub = LightActuator(clientID,broker,port,topic_subscribe_lA)
    lightSub.startSim()
    try:
        while True:        
            time.sleep(10)
    except KeyboardInterrupt:
            lightSub.stopSim()