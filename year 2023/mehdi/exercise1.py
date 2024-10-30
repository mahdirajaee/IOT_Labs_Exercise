import cherrypy 

class HelloWorld(object):
    exposed = True 

    def GET(self, *uri, **params):
        output = "Hello World!" 

       
        if "text" in params:
            output = params["text"][::-1]  
        return output
    
if __name__ == '__main__': 
    conf = { 
        '/': { 
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(), 
            'tools.sessions.on': True 
        } 
    }
    webService = HelloWorld()
    cherrypy.tree.mount(webService, '/', conf) 
    cherrypy.engine.start()
    cherrypy.engine.block()
