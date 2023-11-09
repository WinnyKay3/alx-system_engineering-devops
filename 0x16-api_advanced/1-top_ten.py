#!/usr/bin/python3
"""Titles of first 10 posts listed"""
import requests
import sys


def top_ten(subreddit):
    """Prints top 10 hot posts"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    # provides user agent to identify my script
    headers = {"User-Agent": "MyRedditBot/1.0"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if "data" in data and "children" in data["data"]:
            posts = data["data"]["children"]
            for post in posts:
                print(post["data"]["title"])
    else:
        print(None)  # Prints None for invalid subreddits or other errors


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please pass an argument for subreddit to search.")
    else:
        top_ten(sys.argv[1])
