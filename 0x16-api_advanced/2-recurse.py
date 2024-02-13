#!/usr/bin/python3
""" returns a list of titles of all hot articles """
import requests


def recurse(subreddit, hot_list=[], payload={}):
    """ recursively get all hot_list articles """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'my-app/0.0.1'}
    res = requests.get(url,
                       headers=headers,
                       allow_redirects=False,
                       params=payload)
    if (res.status_code != 200):
        return None
    data = res.json()
    after = data.get('data').get('after')
    if after is None:
        return hot_list
    titles = []
    for post in data.get('data').get('children'):
        titles.append(post.get('data').get('title'))
    return recurse(subreddit, hot_list + titles, {'after': after})
