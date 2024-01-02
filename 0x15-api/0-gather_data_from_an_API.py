#!/usr/bin/python3
"""This Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    locurl = "https://jsonplaceholder.typicode.com/"
    locuser = requests.get(locurl + "users/{}".format(sys.argv[1])).json()
    loctodos = requests.get(locurl + "todos", params={"userId": sys.argv[1]}).json()

    completed = [t.get("title") for t in loctodos if t.get("completed") is True]
    print(
        "Employee {} is done with tasks({}/{}):".format(
            locuser.get("name"), len(completed), len(loctodos)
        )
    )
    [print("\t {}".format(c)) for c in completed]
