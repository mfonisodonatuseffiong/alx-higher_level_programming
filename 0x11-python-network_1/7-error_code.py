#!/usr/bin/python3
"""Send a request to a given URL and display the body of the response.
If the HTTP status code is greater than or equal to 400, print: Error code: followed by the value of the HTTP status code.
Usage: ./7-error_code.py <URL>
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        response = requests.get(url)
        if response.status_code >= 400:
            print(f"Error code: {response.status_code}")
        else:
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
