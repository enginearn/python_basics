#!/usr/bin/env python3

import sys
import http.server
import socketserver

# import webbrowser
# webbrowser.open('http://localhost:8000/')
# b = webbrowser.get('firefox')
# b.open('http://localhost:8000/')

ip_addr = "127.0.0.1"
with socketserver.TCPServer((ip_addr, 8080), http.server.SimpleHTTPRequestHandler) as httpd:
    httpd.serve_forever()

if __name__ == '__main__':
    sys.exit(0)

