#!/usr/bin/python3
"""Send a request to a given URL and display the body of the response.
Usage: ./3-error_code.py <URL>
  - Manage urllib.error.HTTPError exceptions and print: Error code: followed by the HTTP status code.
"""
import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
