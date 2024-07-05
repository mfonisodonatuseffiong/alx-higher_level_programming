#!/usr/bin/python3
"""
Sends a POST request to a given URL with an email as a parameter.
Usage: ./2-post_email.py <URL> <email>
"""
import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./2-post_email.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({"email": email}).encode("ascii")
    request = urllib.request.Request(url, data)

    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
