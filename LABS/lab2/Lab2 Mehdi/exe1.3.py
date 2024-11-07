import cherrypy
import json

class webCalculator:
    exposed = True

    def GET(self, *uri, **params):
        if not uri or len(uri) != 1:
            raise cherrypy.HTTPError(400, "Operation must be specified (add/sub/mul/div)")
        
        operation = uri[0]
        if 'op1' not in params or 'op2' not in params:
            raise cherrypy.HTTPError(400, "Both operands (op1, op2) are required")
        try:
            op1 = float(params['op1'])
            op2 = float(params['op2'])
        except ValueError:
            raise cherrypy.HTTPError(400, "Operands must be valid numbers")
        
        def add(op1, op2):
            return op1 + op2
        
        def sub(self, op1, op2):
            return op1 - op2    
        
        def mul(op1, op2):        
            return op1 * op2

        def div(op1, op2): 
            if op2 == 0:
                raise cherrypy.HTTPError(400, "Division by zero is not allowed")
            return op1 / op2
        
        

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