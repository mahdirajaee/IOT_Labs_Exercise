import paho.mqtt.client as mqtt
import json
import time

broker = 'mqtt.eclipseprojects.io'
port = 1883
topic = 'IoT/your-name/sensor'

# Simulated sensor data in SenML format
sensor_data = [
    {
        "bn": "urn:dev:mac:0024befffe804ff1/",
        "bt": time.time(),
        "e": [
            {"n": "temperature", "u": "Cel", "v": 23.5},
            {"n": "humidity", "u": "%RH", "v": 60}
        ]
    }
]

def on_connect(client, userdata, flags, rc):
    print(f"Connected to {broker} with result code {rc}")

def publish_sensor_data():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect(broker, port, 60)
    client.loop_start()

    try:
        while True:
            sensor_data[0]["bt"] = time.time()  # Update base time
            client.publish(topic, json.dumps(sensor_data))
            print(f"Published sensor data: {sensor_data}")
            time.sleep(5)
    except KeyboardInterrupt:
        client.loop_stop()
        client.disconnect()

if __name__ == '__main__':
    publish_sensor_data()