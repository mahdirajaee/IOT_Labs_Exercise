import cherrypy

class HelloWorld(object):
    exposed = True # DONT FORGET THIS LINE !!
    def __init__(self):
        pass
    def GET (self,*uri,**params):
        #Standard output
        output="Hello World"
        #Check the uri in the requests
        #<br> is just used to append the content in a new line
        #(<br> is the \n for HTML)
        if len(uri)!=0:
            output+='<br>uri: '+'  '.join(uri)
        #Check the parameters in the request
        #<br> is just used to append the content in a new line
        #(<br> is the \n for HTML)
        if params!={}:
            output+='<br>params: '+str(params)
        return output
    def POST (self,*uri,**params):
        pass
    def PUT (self,*uri,**params):
        pass
    def DELETE (self,*uri,**params):
        pass

if __name__=="__main__":
    conf={
        '/':{
            'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on':True
        }
    }
    cherrypy.tree.mount(HelloWorld(),'/',conf)
    cherrypy.config.update({'server.socket_port':8080})
    cherrypy.engine.start()
    cherrypy.engine.block()