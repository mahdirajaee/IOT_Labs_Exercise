import cherrypy
import json
import time

class SensorRESTAPI:
    exposed = True

    def __init__(self):
        self.sensor_data = [
            {
                "bn": "urn:dev:mac:0024befffe804ff1/",
                "bt": time.time(),
                "e": [
                    {"n": "temperature", "u": "Cel", "v": 23.5},
                    {"n": "pressure", "u": "PSI", "v": 200}
                ]
            }
        ]

    @cherrypy.tools.json_out()
    def GET(self):
        self.sensor_data[0]["bt"] = time.time()  # Update base time
        return self.sensor_data  # CherryPy should serialize this to JSON automatically

if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'application/json')],
        }
    }
    cherrypy.tree.mount(SensorRESTAPI(), '/sensor', conf)
    cherrypy.config.update({'server.socket_port': 8080})
    cherrypy.engine.start()
    cherrypy.engine.block()
