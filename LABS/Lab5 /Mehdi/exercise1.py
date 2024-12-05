import cherrypy
import json
import time
import threading
from datetime import datetime, timedelta

class Catalog:
    exposed = True

    def __init__(self):
        # Initialize data storage files
        self.data_file = "catalog.json"
        self.load_data()

        # Start periodic cleanup for outdated devices
        self.cleanup_interval = 60  # Run cleanup every 60 seconds
        self.running = True
        self.cleanup_thread = threading.Thread(target=self.cleanup_devices)
        self.cleanup_thread.start()

    def load_data(self):
        # Load data from JSON file or initialize empty structure
        try:
            with open(self.data_file, "r") as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = {
                "devices": [],
                "users": [],
                "message_broker": {"ip": "127.0.0.1", "port": 1883}
            }
            self.save_data()

    def save_data(self):
        # Save data to JSON file
        with open(self.data_file, "w") as f:
            json.dump(self.data, f, indent=4)

    def cleanup_devices(self):
        # Periodically remove devices with "insert-timestamp" older than 2 minutes
        while self.running:
            time.sleep(self.cleanup_interval)
            cutoff_time = datetime.now() - timedelta(minutes=2)
            self.data["devices"] = [
                device for device in self.data["devices"]
                if datetime.fromisoformat(device["insert-timestamp"]) >= cutoff_time
            ]
            self.save_data()

    @cherrypy.tools.json_out()
    def GET(self, resource=None, identifier=None):
        # Retrieve message broker info
        if resource == "message_broker":
            return self.data["message_broker"]

        # Retrieve all registered devices
        if resource == "devices" and not identifier:
            return self.data["devices"]

        # Retrieve a specific device by ID
        if resource == "devices" and identifier:
            device = next((d for d in self.data["devices"] if d["id"] == identifier), None)
            if device:
                return device
            cherrypy.response.status = 404
            return {"error": "Device not found"}

        # Retrieve all registered users
        if resource == "users" and not identifier:
            return self.data["users"]

        # Retrieve a specific user by ID
        if resource == "users" and identifier:
            user = next((u for u in self.data["users"] if u["id"] == identifier), None)
            if user:
                return user
            cherrypy.response.status = 404
            return {"error": "User not found"}

        cherrypy.response.status = 400
        return {"error": "Invalid request"}

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self, resource=None):
        # Add a new device
        if resource == "devices":
            input_data = cherrypy.request.json
            input_data["insert-timestamp"] = datetime.now().isoformat()  # Add timestamp
            self.data["devices"].append(input_data)
            self.save_data()
            return {"status": "Device added successfully"}

        # Register a new user
        if resource == "users":
            input_data = cherrypy.request.json
            self.data["users"].append(input_data)
            self.save_data()
            return {"status": "User registered successfully"}

        cherrypy.response.status = 400
        return {"error": "Invalid request"}

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def PUT(self, resource=None, identifier=None):
        # Update device information
        if resource == "devices" and identifier:
            device = next((d for d in self.data["devices"] if d["id"] == identifier), None)
            if device:
                input_data = cherrypy.request.json
                device.update(input_data)
                self.save_data()
                return {"status": "Device updated successfully"}
            cherrypy.response.status = 404
            return {"error": "Device not found"}

        cherrypy.response.status = 400
        return {"error": "Invalid request"}

    def stop(self):
        # Stop the periodic cleanup thread
        self.running = False
        self.cleanup_thread.join()

if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'application/json')],
        }
    }
    catalog = Catalog()
    cherrypy.tree.mount(catalog, '/', conf)
    cherrypy.config.update({'server.socket_port': 8080})

    try:
        cherrypy.engine.start()
        cherrypy.engine.block()
    finally:
        catalog.stop()
