import cherrypy 

class helloworld(object):
    exposed = True 
    def GET(self, *uri, **params):
        output = "Hello World!" 

        if len(uri) > 0:
            output += "<br>params: " + str(params)

        if params!={}: 
            output += "<br>params: " + str(params) 

        return output
    
if __name__ == '__main__': 
    conf={ 
        '/':{ 
            'request.dispatch':cherrypy.dispatch.MethodDispatcher(), 
            'tools.sessions.on':True 
        } 
    }
    webService = helloworld()
    cherrypy.tree.mount(webService, '/', conf) 
    cherrypy.engine.start()
    cherrypy.engine.block()

