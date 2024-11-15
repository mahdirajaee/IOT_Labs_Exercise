import paho.mqtt.client as PahoMQTT
import json

class LightManager:
    def __init__(self, clientID, broker, port, alert_topic):
        self.clientID = clientID
        self.broker = broker
        self.port = port
        self.alert_topic = alert_topic
        self.managerClient = PahoMQTT.Client(clientID)
        self.managerClient.on_connect = self.on_connect
        self.managerClient.on_message = self.notify

    def on_connect(self, client, userdata, flags, rc):
        print(f"Connected to {self.broker} with result code {rc}")
        self.managerClient.subscribe(self.alert_topic)

    def notify(self, client, userdata, message):
        alert = json.loads(message.payload.decode('utf-8'))
        print(f"Received alert: {alert}")

    def startSim(self):
        self.managerClient.connect(self.broker, self.port, 60)
        self.managerClient.loop_start()

    def stopSim(self):
        self.managerClient.loop_stop()
        self.managerClient.disconnect()

if __name__ == '__main__':
    broker = 'mqtt.eclipseprojects.io'
    port = 1883
    clientID = 'lightManager'
    alert_topic = 'IoT/your-name/led/alert'
    light_manager = LightManager(clientID, broker, port, alert_topic)
    light_manager.startSim()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Stopping the light manager...")
        light_manager.stopSim()