#!/usr/bin/env python3

import sys
import xmlrpc.client

with xmlrpc.client.ServerProxy('http://localhost:8000') as proxy:
    print(proxy.add_num(1, 2))

if __name__ == '__main__':
    sys.exit(0)

