#!/usr/bin/python 
import SimpleHTTPServer
import SocketServer
import mimetypes

PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

#Handler.extensions_map['.svg']='image/svg+xml'
Handler.extensions_map['.log.1']='text/plain'
httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()