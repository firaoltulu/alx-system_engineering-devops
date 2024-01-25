#!/usr/bin/python3
"""This Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    locuser_id = sys.argv[1]
    locurl = "https://jsonplaceholder.typicode.com/"
    locuser = requests.get(locurl + "users/{}".format(locuser_id)).json()
    username = locuser.get("username")
    loctodos = requests.get(locurl + "todos", params={"userId": locuser_id}).json()

    with open("{}.csv".format(locuser_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [
                writer.writerow([locuser_id, username, t.get("completed"), t.get("title")])
                for t in loctodos
                ]
