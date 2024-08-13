#!/usr/bin/python3
"""This module sends a request
to the Reddit API and returns the number of subscribers
"""
import json
import requests
import sys

import requests.api


def number_of_subscribers(subreddit):
    """This function returns the number of subscribers

    Args:
        subreddit (string): path to subreddit to get subscribers
    """

    if len(sys.argv) < 2:
        return 0
    else:
        res = requests.get('https://www.reddit.com/r/{}/about.json'.format(subreddit),
                           headers={'User-Agent': "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}, allow_redirects=False)
        if res.status_code != 200:
            return 0
        res = res.json().get("data").get("subscribers")
        print(res)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(0)
    else:
        number_of_subscribers(sys.argv[1])
