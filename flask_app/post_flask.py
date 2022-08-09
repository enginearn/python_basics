#!/usr/bin/env python3

import sys
import requests

r = requests.post('http://127.0.0.1:5000/post', data={"user_name": "John"})
print(r.text)

if __name__ == '__main__':
    sys.exit(0)

