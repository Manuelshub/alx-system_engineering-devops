#!/usr/bin/python3
"""
Prints the title of the first 10 hot posts listed in the subreddit
"""
import requests


def top_ten(subreddit):
    """
    Queriest the Reddit API and prints the titles of the first ten
    hot posts in the given subreddit.
    """
    if not subreddit or not isinstance(subreddit, str):
        print('None')

    url = f"https://www.reddit.com/r/{subreddit}/top.json"
    user_agent = {'User-Agent': 'Google Chrome Version 125.0.6422.141'}

    request = requests.get(url, headers=user_agent)
    response = request.json()

    try:
        data = response.get('data').get('children')
        for post in data[:10]:
            print(post['data']['title'])
    except Exception:
        print('None')
