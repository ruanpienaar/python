#!/usr/bin/env python

import cgi, os, SocketServer, sys, time, urllib, json, socket
from SimpleHTTPServer import SimpleHTTPRequestHandler
from StringIO import StringIO
from threading import Thread
from time import sleep

class JsonHandler(SimpleHTTPRequestHandler):
    def list_directory(self, path):
        try:
            list = os.listdir(path)
        except os.error:
            self.send_error(404, "No permission to list directory")
            return None
        list.sort(key=lambda a: a.lower())
        displaypath = cgi.escape(urllib.unquote(self.path))
        jsonFiles = []
        ip=socket.gethostbyname(socket.gethostname())
        for name in list:
            fullname = os.path.join(path, name)
            displayname = linkname = name
            date_modified = time.ctime(os.path.getmtime(fullname))
            # Append / for directories or @ for symbolic links
            if os.path.isdir(fullname):
                displayname = name + "/"
                linkname = name + "/"
            if os.path.islink(fullname):
                displayname = name + "@"
            absurl= "http://" + ip + ":9998/" + urllib.quote(linkname)
            jsonFiles.append({'date_modified':date_modified,'url':absurl,'filename':cgi.escape(displayname)})
        json_data = json.dumps(jsonFiles, separators=(',',':'))
        f = StringIO()
        f.write('%s' % json_data)
        length = f.tell()
        f.seek(0)
        self.send_response(200)
        encoding = sys.getfilesystemencoding()
        self.send_header("Content-type", "application/json; charset=%s" % encoding)
        self.send_header("Content-Length", str(length))
        self.end_headers()
        return f

httpd = SocketServer.TCPServer(("", 9998), JsonHandler)
print "serving at port", 9998
httpd.serve_forever()