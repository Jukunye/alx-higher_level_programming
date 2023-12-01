#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response
(decoded in utf-8)
"""

from sys import argv
from urllib import request, parse

if __name__ == "__main__":
    data_dict = {'email': argv[2]}
    data = parse.urlencode(data_dict).encode()

    with request.urlopen(argv[1], data=data) as response:
        html = response.read()
        print(html.decode(encoding='utf-8'))
