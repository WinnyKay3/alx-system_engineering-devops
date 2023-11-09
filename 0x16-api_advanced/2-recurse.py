#!/usr/bin/python3
""" Querys reddit API"""
import requests
import sys


def recurse(subreddit, hot_list=[], after=None):
    """a recursive func that retrieves all hot titles"""
    if len(hot_list) == 0:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    else:
        url = (
            f"https://www.reddit.com/r/{subreddit}/hot.json?" f"limit=10&after={after}"
        )

        headers = {"User-Agent": "MyRedditBot/1.0"}

        response = request.get(url, headers=headers)

        # checks if request is successful
        if response.status_code == 200:
            data = response.json()
            if "data" in data and "children" in data["data"]:
                posts = data["data"]["children"]
                if len(posts) == 0:
                    return hot_list
                else:
                    for post in posts:
                        hot_list.append(post["data"]["title"])
                    last_post_id = posts[-1]["data"]["name"]
                    return recurse(subreddit, hot_list, last_post_id)
            else:
                return None
        else:
            return None


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
