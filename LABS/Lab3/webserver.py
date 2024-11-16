import cherrypy
import json 


class calculatorWebServer: 
    exposed = True 
    def GET(self, *uri, **params):
        if len(uri) == 1 : 
            pass
