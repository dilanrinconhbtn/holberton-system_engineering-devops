#!/usr/bin/python3
"""number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """ number of subs"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    headers = {"User-Agent": "dilanrincon"}
    request = requests.get('https://api.reddit.com/r/{}/about'.
                           format(subreddit),
                           headers=headers)
    if subRinfo.status_code == 404:
        return 0
    subs = request.join()
    sub = subs['data']['subscribers']
    return sub
