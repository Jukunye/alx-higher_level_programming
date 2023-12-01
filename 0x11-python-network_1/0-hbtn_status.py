#!/usr/bin/python3
# script that fetches https://alx-intranet.hbtn.io/status

from urllib.request import urlopen

with urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
    print('Body response:')
    print('\t- type: ', type(html))
    print('\t- content: ', html)
    print('\t- utf8 content: ', html.decode(encoding='utf-8'))
