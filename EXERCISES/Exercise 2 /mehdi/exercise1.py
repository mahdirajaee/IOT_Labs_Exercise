
import cherrypy
import json 

def reverse_string(text_to_reverse):
    return text_to_reverse[::-1] # [a:b:step] going from a to b using a step equal to step


class StringReverser:
    exposed=True
    def __init__(self):
        pass


    def GET(self,*uri,**params):
        output=''
        if len(uri)>0:
            output= ''
            for pathi in uri:
                output+=reverse_string(pathi)+'<br>'
            return output
        else:
            raise cherrypy.HTTPError(500)
        

    def PUT(self,*uri,**params):
        try : 
            body = cherrypy.request.body.read().decode('utf-8') 
            reverse_string = reverse_string(body) 
            response = {'reversed_string': reverse_string}
            cherrypy.response.headers['Content-Type'] = 'application/json'
            return json.dumps(response) 
        except Exception as e:
            raise cherrypy.HTTPError(500, str(e))
        

    def POST(self,*uri,**params):
        pass

if __name__ == '__main__':
    conf={
        #Standard configuration to serve the url "localhost:8080"
            '/':{
            'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on':True
            }
        }
    webService=StringReverser()
    cherrypy.tree.mount(webService,'/',conf)
    cherrypy.engine.start()
    cherrypy.engine.block()