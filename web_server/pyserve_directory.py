#!/usr/bin/env python

import cgi, os, SocketServer, sys, time, urllib, mimetypes, posixpath, getopt
from SimpleHTTPServer import SimpleHTTPRequestHandler
from StringIO import StringIO

class DirectoryHandler(SimpleHTTPRequestHandler):

    def send_head(self):
        path = self.translate_path(self.path)
        f = None
        if os.path.isdir(path):
            for index in "index.html", "index.htm":
                index = os.path.join(path, index)
                if os.path.exists(index):
                    path = index
                    break
            else:
                return self.list_directory(path)
        ctype = self.guess_type(path)
        if ctype.startswith('text/'):
            mode = 'r'
        else:
            mode = 'rb'
        try:
            f = open(path, mode)
        except IOError:
            self.send_error(404, "File not found")
            return None
        self.send_response(200)
        self.send_header("Content-type", ctype)
        self.end_headers()
        return f
        
    def guess_type(self, path):
        base, ext = posixpath.splitext(path)
        if self.extensions_map.has_key(ext):
            return self.extensions_map[ext]
        ext = ext.lower()
        if self.extensions_map.has_key(ext):
            return self.extensions_map[ext]
        else:
            return self.extensions_map['']

    extensions_map = mimetypes.types_map.copy()
    extensions_map.update({
        '': 'text/plain'
        })

    def list_directory(self, path):
        try:
            list = os.listdir(path)
        except os.error:
            self.send_error(404, "No permission to list directory")
            return None
        list.sort(key=lambda a: a.lower())
        f = StringIO()
        displaypath = cgi.escape(urllib.unquote(self.path))
        f.write('<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">')
        f.write("<html>\n<title>Directory listing for %s</title>\n" % displaypath)
        f.write("<body>\n")
        f.write("<table>\n<captian><h2>Directory listing for %s</h2></captian>\n<thead><tr><th>Date Modified</th><th>Filename</th></tr></thead><tbody>" % displaypath)
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
                # Note: a link to a directory displays with @ and links with /
            f.write('<tr><td>%s</td><td><a href="%s">%s</a></td></tr>\n'
                    % (date_modified, urllib.quote(linkname), cgi.escape(displayname)))
        f.write("</tbody></table>\n<hr>\n</body>\n</html>\n")
        length = f.tell()
        f.seek(0)
        self.send_response(200)
        encoding = sys.getfilesystemencoding()
        self.send_header("Content-type", "text/html; charset=%s" % encoding)
        self.send_header("Content-Length", str(length))
        self.end_headers()
        return f

def usage():
    print 'usage: pyserve_directory.py -p/--port=PORT -d/--dir=DIR OR -h'

def main(restArgs):
    port=''
    dir=''
    try:
        if len(restArgs) != 2:
            raise ValueError('missing arguments')
        opts, args = getopt.getopt(restArgs,"hp:d:",["port=","dir="])
        for opt, arg in opts:
            if opt == '-h':
                usage()
            elif opt in ("-p", "--port"):
                port = arg
            elif opt in ("-d", "--dir"):
                dir = arg
                os.chdir(arg)
        print "Serving port %s from directory %s" % (port, dir)
        httpd = SocketServer.TCPServer(("", int(port)), DirectoryHandler)
        httpd.serve_forever()
    except getopt.GetoptError:
        usage()
    except Exception:
        print Exception
        usage()
    
if __name__ == "__main__":
     main(sys.argv[1:])

