#!/usr/bin/python3
"""This module sends a request
to the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """This function returns the number of subscribers
    Args:
        subreddit (string): path to subreddit to get subscribers
    """
    res = requests.get('https://www.reddit.com/r/{}/about.json'.format(subreddit),
                       headers={'User-Agent': "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}, allow_redirects=False)
    if res.status_code == 404:
        return 0
    res = res.json().get("data").get("subscribers")
    return res
