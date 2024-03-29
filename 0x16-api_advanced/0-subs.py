#!/usr/bin/python3
""" querry reddit api to get number of subscribers """
import requests


def number_of_subscribers(subreddit):
    """ get number of subscriberts of subreddit """
    headers = {'User-Agent': 'my-app/0.0.1'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        return 0
    else:
        data = res.json()
        return data.get('data').get('subscribers')
