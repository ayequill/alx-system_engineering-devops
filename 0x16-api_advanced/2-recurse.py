#!/usr/bin/python3
""" Queries top 10 posts in a subreddit """
from requests import get, exceptions


def recurse(subreddit, hot_list=None, nxt=None):
    """ Queries top 10 posts in a subreddit recursively"""
    if hot_list is None:
        hot_list = []
    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    if nxt:
        url += "&after={}".format(nxt)
    try:
        res = get(url, headers={'User-Agent': 'Safari 20'},
                  allow_redirects=False)
        res.raise_for_status()
        if res.status_code == 200:
            data = res.json()
            if data.get('data').get('children'):
                posts = data.get('data').get('children')
                if len(posts) == 0:
                    return hot_list
                hot_list.extend([post['data']['title'] for post in posts])
                if data.get('data').get('after'):
                    nxt = data['data']['after']
                    return recurse(subreddit, hot_list, nxt)
                else:
                    return hot_list
    except exceptions.HTTPError:
        return None
