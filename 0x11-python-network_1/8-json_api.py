#!/usr/bin/python3
"""Send a POST request to http://0.0.0.0:5000/search_user with a given letter.
Usage: ./8-json_api.py <letter>
  - The letter must be sent in the variable q.
  - If no argument is given, set q="".
  - If the response body is properly JSON formatted and not empty,
    display the id and name like this: [<id>] <name>.
  - Otherwise:
    - Display Not a valid JSON if the JSON is invalid.
    - Display No result if the JSON is empty.
"""
import sys
import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    payload = {'q': letter}

    try:
        response = requests.post(url, data=payload)
        response_json = response.json()
        
        if response_json:
            print(f"[{response_json.get('id')}] {response_json.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
