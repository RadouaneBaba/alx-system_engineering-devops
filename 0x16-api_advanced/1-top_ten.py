#!/usr/bin/python3
""" hot posts titles """
import requests


def top_ten(subreddit):
    """ top ten hot posts title """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'my-app/0.0.1'}
    res = requests.get(url, headers=headers, allow_redirects=False)
    if (res.status_code != 200):
        print(None)
    else:
        data = res.json()
        for post in data.get('data').get('children'):
            print(post.get('data').get('title'))
