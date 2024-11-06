import cherrypy
import json

def string_reverse(string):
    #there is a python function that does this: reversed(string)
    return string[::-1] # [a:b:step] going from a to b using a step equal to step

class StringReverse(object):
    exposed = True
    def __init__(self):
        pass
    def GET(self,*uri,**params):
        pass     
    def POST(self,*uri,**params):
        pass
    def PUT(self,*uri,**params):
        body=cherrypy.request.body.read()
        if len(body)>0:
            try:
                jsonBody=json.loads(body)
                for key in jsonBody.keys():
                    jsonBody[key]= string_reverse(jsonBody[key])
                return json.dumps(jsonBody)
            except json.decoder.JSONDecodeError:
                raise cherrypy.HTTPError(400,"Bad Request. Body must be a valid JSON")
            except:
                raise cherrypy.HTTPError(500,"Internal Server Error")
        else:
            return "Empty Body"
    def DELETE(self,*uri,**params):
        pass

if __name__=="__main__":
    conf={
        '/':{
            'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on':True
        }
    }
    cherrypy.tree.mount(StringReverse(),'/',conf)
    cherrypy.config.update({'server.socket_port':8080})
    cherrypy.engine.start()
    cherrypy.engine.block()