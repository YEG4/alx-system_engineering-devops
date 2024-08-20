#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import json
import requests

# def recurse(subreddit, hot_list=[], after="", count=0):
#     """Returns a list of titles of all hot posts on a given subreddit."""
#     url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
#     headers = {
#         "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
#     }
#     params = {
#         "after": after,
#         "count": count,
#         "limit": 100
#     }
#     response = requests.get(url, headers=headers, params=params,
#                             allow_redirects=False)
#     if response.status_code == 404:
#         return None

#     results = response.json().get("data")
#     after = results.get("after")
#     count += results.get("dist")
#     for c in results.get("children"):
#         hot_list.append(c.get("data").get("title"))

#     if after is not None:
#         return recurse(subreddit, hot_list, after, count)
#     return hot_list


# def recurse(subreddit, hot_list=[], after="", count=0):
#     url = 'https://www.reddit.com/r/{}/hot.json'
#     res = requests.get(url.format(subreddit), params={"raw_json": 1}, headers={
#                        "User-Agent": "Mozilla/5.0"}, allow_redirects=False)
#     response = json.loads(res.content).get('data')
#     after = response.get('after')
#     count += response.get('dist')
#     new_response = requests.get(url.format(subreddit), params={
#                                 'after': after, 'count': count}, headers={"User-Agent": "Mozilla/5.0"}, allow_redirects=False)
#     print(new_response.json().get('data'))
#     # children = response.get('children')

#     # for child in children:
#     #     print(child.get('data').get('title'))


# recurse('programming')
