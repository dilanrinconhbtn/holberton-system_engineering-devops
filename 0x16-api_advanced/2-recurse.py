#!/usr/bin/python3
"""list all hot articles"""
import requests


def recurse(subreddit, hot_list=[], next_pg=None):
    """hot posts"""
    headers = {"User-Agent": "dilanrincon"}

    if next_pg:
        request = requests.get('https://reddit.com/r/' +
                               subreddit +
                               '/hot.json?after=' + 
                               next_pg,
                               headers=headers)
    else:
        request = requests.get('https://reddit.com/r/' + 
                               subreddit +
                               '/hot.json',
                               headers=headers)

    if request.status_code == 404:
        return None
    request_dict = request.json()
    request_data = request_dict['data']
    next_pg = request_data['after']
    request_posts = request_data['children']
    for post in request_posts:
        post_data = post['data']
        hot_list.append(post_data['title'])

    if next_pg:
        recurse(subreddit, hot_list, next_pg)
    return hot_list