#!/bin/python
'''
Simple web server
'''

import SimpleHTTPServer
import SocketServer

PORT = 80

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print("serving at port{}".format(PORT))
httpd.serve_forever()
