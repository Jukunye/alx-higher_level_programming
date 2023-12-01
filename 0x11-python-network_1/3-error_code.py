#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
"""

import urllib
from sys import argv
from urllib.request import urlopen

if __name__ == "__main__":
    try:
        with urlopen(argv[1]) as response:
            html = response.read()
            print(html.decode(encoding='utf-8'))
    except urllib.error.HTTPError as e:
        print(e.getcode())
