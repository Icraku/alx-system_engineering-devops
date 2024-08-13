#!/usr/bin/python3
"""
Module for task 0
"""

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers to the subreddit
    """
    import requests

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            "User-Agent": "python:subreddit.subscriber.counter:v1.0 (by /u/Mysterious-Fix-4680)"
            }

    try:
        sub_info = requests.get(url, headers, allow_redirects=False)
        if sub_info.status_code == 200:
            return sub_info.json().get("data", {}).get("subscribers", 0)
        else:
            print(f"Request failed with status code: {sub_info.status_code}")
            return 0
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return 0
