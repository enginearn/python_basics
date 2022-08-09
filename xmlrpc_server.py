#!/usr/bin/env python3

import sys
import xmlrpc.server

with xmlrpc.server.SimpleXMLRPCServer(('127.0.0.1', 8000)) as server:
    def add_num(x, y):
        return x + y

    server.register_function(add_num, 'add_num')
    server.serve_forever()

if __name__ == '__main__':
    sys.exit(0)

