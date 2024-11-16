import cherrypy
import json

class CalculatorServer:
    cherrypy.expoed = True 

    def add(self, op1, op2):
        """Endpoint for addition."""
        op1 = float(op1)
        op2 = float(op2)
        result = op1 + op2
        return json.dumps({"operation": "add", "op1": op1, "op2": op2, "result": result})

    def subtract(self, op1, op2):
        """Endpoint for subtraction."""
        op1 = float(op1)
        op2 = float(op2)
        result = op1 - op2
        return json.dumps({"operation": "subtract", "op1": op1, "op2": op2, "result": result})

    def multiply(self, op1, op2):
        """Endpoint for multiplication."""
        op1 = float(op1)
        op2 = float(op2)
        result = op1 * op2
        return json.dumps({"operation": "multiply", "op1": op1, "op2": op2, "result": result})

    def divide(self, op1, op2):
        """Endpoint for division."""
        op1 = float(op1)
        op2 = float(op2)
        if op2 == 0:
            return json.dumps({"error": "Division by zero is not allowed"})
        result = op1 / op2
        return json.dumps({"operation": "divide", "op1": op1, "op2": op2, "result": result})

if __name__ == "__main__":
    config = {
        'global': {
            'server.socket_host': '0.0.0.0',
            'server.socket_port': 8080,
            'server.thread_pool': 8,
            'log.screen': True,
        },
        '/': {
            'tools.sessions.on': True,
            'tools.sessions.timeout': 60,
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'application/json')],
        }
    }
    cherrypy.quickstart(CalculatorServer(), '/', config)