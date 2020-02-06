#!/usr/bin/python3
"""number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """ number of subs"""
    headers = {"User-Agent": "dilanrincon"}
    request = requests.get('https://api.reddit.com/r/{}/about'.
                           format(subreddit),
                           headers=headers)
    if request.status_code == 404:
        return 0
    subs = request.json()
    sub = subs['data']['subscribers']
    return sub
