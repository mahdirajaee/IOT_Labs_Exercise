import json
import cherrypy
import requests

def reverse_string(s):
    return s[::-1]

class StringReverser:
    exposed = True

    r = requests.get('https://catalog-p4iot.onrender.com/')
    r.text()
    r.json()

    def PUT(self, *uri, **params):
        try:
           
            body = cherrypy.request.body.read().decode('utf-8')
            data = json.loads(body)
            reversed_data = {key: reverse_string(value) for key, value in data.items()}
            cherrypy.response.headers['Content-Type'] = 'application/json'
            return json.dumps(reversed_data).encode('utf-8')  

        except Exception as e:
            raise cherrypy.HTTPError(500, str(e))

if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True
        }
    }
    cherrypy.tree.mount(StringReverser(), '/', conf)
    cherrypy.engine.start()
    cherrypy.engine.block()
