import cherrypy
import json
import time
import threading
import random

class SensorRESTAPI:
    exposed = True
    
    def __init__(self):
        # Initialize sensor data
        self.sensor_data = [
            {
                "bn": "http://127.0.0.1:8080/sensor",
                "bt": time.time(),
                "e": [
                    {"n": "temperature", "u": "Cel", "v": 23.5},
                    {"n": "pressure", "u": "PSI", "v": 200}
                ]
            }
        ]
        # Start a thread to update sensor values periodically
        self.running = True
        self.update_thread = threading.Thread(target=self.update_sensor_values)
        self.update_thread.start()

    def update_sensor_values(self):
        while self.running:
            # Update the sensor data periodically (e.g., every 5 seconds)
            time.sleep(5)
            self.sensor_data[0]["bt"] = time.time()
            self.sensor_data[0]["e"][0]["v"] = round(random.uniform(20.0, 30.0), 1)  # Temperature
            self.sensor_data[0]["e"][1]["v"] = round(random.uniform(180.0, 220.0), 1)  # Pressure
            print("Updated sensor data:", self.sensor_data)  # Log the updates for debugging

    @cherrypy.tools.json_out()
    def GET(self):
        # Serve the latest sensor data
        return self.sensor_data

    def stop(self):
        # Stop the thread when the server shuts down
        self.running = False
        self.update_thread.join()

if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'application/json')],
        }
    }
    # Create an instance of the SensorRESTAPI class
    sensor_api = SensorRESTAPI()
    cherrypy.tree.mount(sensor_api, '/sensor', conf)
    cherrypy.config.update({'server.socket_port': 8080})

    try:
        cherrypy.engine.start()
        cherrypy.engine.block()
    finally:
        sensor_api.stop()  # Ensure the thread stops when the server is stopped
