import cherrypy
import json

class ReverseService(object):
    exposed = True

    def PUT(self):
        # Get the JSON data from the request body
        content_length = cherrypy.request.headers.get('Content-Length', 0)
        raw_body = cherrypy.request.body.read(int(content_length))
        
        try:
            # Parse JSON data
            data = json.loads(raw_body)
            
            # Reverse each value in the JSON data
            reversed_data = {key: value[::-1] for key, value in data.items()}
            
            # Return the reversed JSON as a response
            cherrypy.response.headers['Content-Type'] = 'application/json'
            return json.dumps(reversed_data)
        
        except json.JSONDecodeError:
            # Handle case where the request body is not valid JSON
            cherrypy.response.status = 400
            return json.dumps({"error": "Invalid JSON data"})
        
         
    
if __name__ == '__main__':
    conf = { 
        '/': { 
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'application/json')],
        }
    }
    cherrypy.tree.mount(ReverseService(), '/', conf)
    cherrypy.engine.start()
    cherrypy.engine.block()
