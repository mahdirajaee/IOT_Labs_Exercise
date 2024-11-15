import paho.mqtt.client as PahoMQTT
import json

class LightActuatorPublisher:
    def __init__(self, clientID, broker, port, topic_publish, topic_subscribe, alert_topic):
        self.clientID = clientID
        self.broker = broker
        self.port = port
        self.topic_publish = topic_publish
        self.topic_subscribe = topic_subscribe
        self.alert_topic = alert_topic
        self.publisherClient = PahoMQTT.Client(clientID)
        self.publisherClient.on_connect = self.on_connect
        self.publisherClient.on_message = self.notify
        self.light_status = "OFF"  # we consider the light is initailly off

    def on_connect(self, client, userdata, flags, rc):
        print(f"Connected to {self.broker} with result code {rc}")
        self.publisherClient.subscribe(self.topic_subscribe)

    # would act as the checker whether the light is on or off 
    def notify(self, client, userdata, message):
        command = json.loads(message.payload.decode('utf-8'))
        print(f"Received command: {command}")
        if command["status"] == self.light_status:
            alert_message = {"alert": f"Light is already {self.light_status}"}
            self.publisherClient.publish(self.alert_topic, json.dumps(alert_message), 2)
            print(f"Published alert: {alert_message}")
        else:
            self.light_status = command["status"]
            self.publish(command)

    def startSim(self):
        self.publisherClient.connect(self.broker, self.port, 60)
        self.publisherClient.loop_start()
    
    def stopSim(self):
        self.publisherClient.loop_stop()
        self.publisherClient.disconnect()

    def publish(self, message_to_publish):
        self.publisherClient.publish(self.topic_publish, json.dumps(message_to_publish), 2)
        print(f"Published message: {message_to_publish}")

if __name__ == '__main__':
    broker = 'mqtt.eclipseprojects.io'
    port = 1883
    clientID = 'lightActuator'
    topic_publish = 'IoT/your-name/led/status'
    topic_subscribe = 'IoT/your-name/led/command'
    alert_topic = 'IoT/your-name/led/alert'
    light_actuator = LightActuatorPublisher(clientID, broker, port, topic_publish, topic_subscribe, alert_topic)
    light_actuator.startSim()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Stopping the light actuator...")
        light_actuator.stopSim()