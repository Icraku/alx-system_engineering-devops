#!/usr/bin/python3
"""
Module for task 1
"""

def top_ten(subreddit):
    """Queries the Reddit API and returns the top 10 hot posts 
    of the subreddit
    """
    import requests

    sub_info = requests.get(
            "https://www.reddit.com/r/{}/hot.json?limit=10"
            .format(subreddit),
            headers={"User-Agent": "Mysterious-Fix-4680"},
            allow_redirects=False)
    if sub_info.status_code >= 300:
        print('None')
    else:
        [print(child.get("data").get("title"))
                for child in sub_info.json()
                .get("data").get("children")]
