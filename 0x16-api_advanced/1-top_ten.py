#!/usr/bin/python3
"""titles of the first 10 hot posts listed"""
import requests
import sys


def top_ten(subreddit):
    """Print top 10 posts"""
    headers = {"User-Agent": "dilanrincon"}
    request = requests.get('https://reddit.com/r/' +
                           subreddit +
                           '/hot.json?sort=hot&limit=10',
                           headers=headers)
    if request.status_code == 404:
        print(None)
        return

    request_dict = request.json()
    request_data = request_dict['data']
    request_posts = request_data['children']

    for post in request_posts:
        post_data = post['data']
        print(post_data['title'])
