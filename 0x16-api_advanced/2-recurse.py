#!/usr/bin/python3
"""
Returns a list containing the titles of all hot articles in a subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return None

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    user_agent = {'User-Agent': 'Google Chrome Version 125.0.6422.141'}
    params = {}

    if after:
        params['after'] = after

    try:
        request = requests.get(url, headers=user_agent, params=params)
        response = request.json()

        for post in response.get('data').get('children'):
            hot_list.append(post['data']['title'])

        if response['data'].get('after'):
            recurse(subreddit, hot_list, after=response['data']['after'])

        return hot_list
    except Exception:
        return None

