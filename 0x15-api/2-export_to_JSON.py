#!/usr/bin/python3
"""This Exports to-do list information for a given employee ID to JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    locuser_id = sys.argv[1]
    locurl = "https://jsonplaceholder.typicode.com/"
    locuser = requests.get(locurl + "users/{}".format(locuser_id)).json()
    locusername = locuser.get("username")
    loctodos = requests.get(locurl + "todos", params={"userId": locuser_id}).json()

    with open("{}.json".format(locuser_id), "w") as jsonfile:
        json.dump(
                {
                    locuser_id: [
                        {
                            "task": t.get("title"),
                            "completed": t.get("completed"),
                            "username": locusername,
                            }
                        for t in loctodos
                        ]
                    },
                jsonfile,
                )
