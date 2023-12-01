#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
from sys import argv

if __name__ == "__main__":
    try:
        data_dict = {'q': argv[1]}
    except IndexError:
        data_dict = {'q': ""}

    response = requests.post('http://0.0.0.0:5000/search_user', data=data_dict)
    json_data = response.json()

    if not json_data:
        print("No result")
    else:
        try:
            print("[{}] {}".format(json_data['id'], json_data['name']))
        except KeyError:
            print("Not a valid JSON")
