import cherrypy 
import json 

class webCalculator: 
    exposed = True 
    operands = []
    operation = None
    def GET(self, *uri, **params):
        pass


    def add(self, operation, operands):
        json.dumps({"operation": operation, "operand1": operands[0], "operand2": operands[1], "result": operation(operands[0], operands[1])})   
        return operation(operands[0], operands[1])

    
    def sub(self, operation, operands):
        return operation(operands[0], operands[1]) 
    
    def mul(self, operation, operands):
        return operation(operands[0], operands[1]) 
    
    def div(self, operation, operands): 
        return operation(operands[0], operands[1]) 
    
   



if __name__=="__main__":
    conf={
        '/':{
            'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on':True
        }
    }
    cherrypy.tree.mount(webCalculator(),'/',conf)
    cherrypy.config.update({'server.socket_port':8080})
    cherrypy.engine.start()
    cherrypy.engine.block()