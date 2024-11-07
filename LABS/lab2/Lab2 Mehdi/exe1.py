import json
import cherrypy

def reverse_string(s):
    return s[::-1]

class StringReverser:
    exposed = True

    def PUT(self, *uri, **params):
        try:
            body = cherrypy.request.body.read().decode('utf-8')
            data = json.loads(body)
            reversed_data = {key: reverse_string(value) for key, value in data.items()}
            cherrypy.response.headers['Content-Type'] = 'application/json'
            return json.dumps(reversed_data).encode('utf-8')  
        except Exception as e:
            raise cherrypy.HTTPError(500, str(e))

class Calculator:
    exposed = True

    def GET(self, *uri, **params):
        if len(uri) < 3:
            raise cherrypy.HTTPError(400, "Insufficient parameters")
        
        operation = uri[0]
        try:
            operand1 = float(uri[1])
            operand2 = float(uri[2])
        except ValueError:
            raise cherrypy.HTTPError(400, "Operands must be numbers")

        result = None
        if operation == "add":
            result = operand1 + operand2
        elif operation == "sub":
            result = operand1 - operand2
        elif operation == "mul":
            result = operand1 * operand2
        elif operation == "div":
            if operand2 == 0:
                raise cherrypy.HTTPError(400, "Division by zero is not allowed")
            result = operand1 / operand2
        else:
            raise cherrypy.HTTPError(400, "Invalid operation")

        response = {"operation": operation, "operand1": operand1, "operand2": operand2, "result": result}
        cherrypy.response.headers['Content-Type'] = 'application/json'
        return json.dumps(response).encode('utf-8')

if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True
        }
    }
    cherrypy.tree.mount(StringReverser(), '/reverse', conf)
    cherrypy.tree.mount(Calculator(), '/calc', conf)
    cherrypy.engine.start()
    cherrypy.engine.block()
