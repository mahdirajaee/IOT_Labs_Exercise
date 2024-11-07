import cherrypy
import json

class webCalculator:
    exposed = True

    def GET(self, *uri, **params):
    
        if len(uri) != 3:
            raise cherrypy.HTTPError(400, "Operation and two operands must be specified in the format /operation/op1/op2")
        
        operation = uri[0]
        
        try:
            op1 = float(uri[1])
            op2 = float(uri[2])
        except ValueError:
            raise cherrypy.HTTPError(400, "Operands must be valid numbers")
        
        
        result = None
        if operation == "add":
            result = op1 + op2
        elif operation == "sub":
            result = op1 - op2
        elif operation == "mul":
            result = op1 * op2
        elif operation == "div":
            if op2 == 0:
                raise cherrypy.HTTPError(400, "Division by zero is not allowed")
            result = op1 / op2
        else:
            raise cherrypy.HTTPError(400, "Invalid operation. Use add/sub/mul/div")
        
      
        response = {
            "operation": operation,
            "op1": op1,
            "op2": op2,
            "result": result
        }
        
        
        cherrypy.response.headers['Content-Type'] = 'application/json'
        return json.dumps(response).encode('utf-8')

if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'application/json')],
        }
    }
    
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.config.update({'server.socket_port': 8080})
    
    cherrypy.quickstart(webCalculator(), '/', conf)