from http.server import HTTPServer
from http.server import SimpleHTTPRequestHandler
HTTP_Version = 'HTTP/1.1'
SP           = ' '
CRLF         = '\r\n'
import os

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        Status_Code = ''
        Reason_Phrase = ''

        if self.command == 'GET':
            localPath = '.' + self.path
            print('file path>.' + localPath)
            if(os.path.isfile(localPath)):
                print('file path>.' + localPath)
            else:
                print('404 Not Found')
                Status_Code = '404'
                Reason_Phrase = 'Not Found'
            pass
        else:
            Status_Code = '501'
            Reason_Phrase = 'Not Implemented'
        pass
    
        Status_Line   = HTTP_Version + SP + Status_Code + SP + Reason_Phrase + CRLF
        media_type    = 'text/html'
        Content_Type  = "Content-Type"+":"+media_type+";"+"charset=utf-8"
        entity_header = Content_Type + CRLF
        Response      = Status_Line + entity_header + CRLF
        html          = bytes(Response, encoding='utf-8')
        
        self.wfile.write(html)

ip = '127.0.0.1'
port = 8000

handler = CustomHandler
server = HTTPServer((ip, port), handler)

server.serve_forever()
