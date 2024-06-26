#!/usr/bin/python3
"""
Returns the number of subscribers for a subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a subreddit.
    """
    if not subreddit or not isinstance(subreddit, str):
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    user_agent = {'user-agent': 'Google Chrome Version 125.0.6422.141'}

    request = requests.get(url=url, headers=user_agent, allow_redirects=False)
    res = request.json()

    try:
        request = requests.get(url=url, headers=user_agent,
                               allow_redirects=False)
        res = request.json()
        return res.get('data').get('subscribers')
    except Exception:
        return 0
