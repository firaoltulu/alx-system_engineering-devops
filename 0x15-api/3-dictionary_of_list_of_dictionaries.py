#!/usr/bin/python3
"""This Exports to-do list information of all employees to JSON format."""
import json
import requests

if __name__ == "__main__":
    locurl = "https://jsonplaceholder.typicode.com/"
    locusers = requests.get(locurl + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(
                {
                    u.get("id"): [
                        {
                            "task": t.get("title"),
                            "completed": t.get("completed"),
                            "username": u.get("username"),
                            }
                        for t in requests.get(
                            locurl + "todos", params={"userId": u.get("id")}
                            ).json()
                        ]
                    for u in locusers
                    },
                jsonfile,
                )
