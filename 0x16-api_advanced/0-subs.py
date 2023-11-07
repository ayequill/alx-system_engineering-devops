#!/usr/bin/python3
""" Queries and return the number of subscribers in sub reddit """
from requests import get


def number_of_subscribers(subreddit):
    """ Queries the reddit API"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = get(url, headers={'User-Agent': 'Mozilla/5.0'})
    if res.ok:
        data = res.json()
        if data.get('data').get('subscribers'):
            return int(data['data']['subscribers'])
        else:
            return 0
    else:
        return 0
