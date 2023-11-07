#!/usr/bin/python3
""" Queries top 10 posts in a subreddit """
from requests import get


def top_ten(subreddit):
    """ Queries top 10 posts in a subreddit """
    url = "https://www.reddit.com/r/{}/top.json?limit=10".format(subreddit)
    res = get(url, headers={'User-Agent': 'Mozilla/5.0'})
    data = res.json()
    if res.ok:
        if data.get('data').get('children'):
            [print(post['data']['title']) for post in data['data']['children']]
        else:
            print(None)
    else:
        print(None)
