import cherrypy 

class HelloWorld(object):
    exposed = True 

    def GET(self, *uri, **params):
        if len(uri) > 0:
            # Take the first part of the URI and reverse it
            output = uri[0][::-1]
        else:
            output = "Hello World!"  # Default message if no URI segment is provided
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
