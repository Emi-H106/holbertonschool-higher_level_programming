#!/usr/bin/env python3
"""
This module provides functions to fetch post data from the JSONPlaceholder API,
print their titles, and save them to a CSV file.
"""

import requests
import csv


def fetch_and_print_posts():
    """
    Fetches post data from JSONPlaceholder and prints
    the title of each post.
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
          posts = response.json()
          for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    """
    Fetches post data from JSONPlaceholder and saves it to
    a CSV file named 'posts.csv', including the post's
    id, title, and body.
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
          posts = response.json()
          post_list = [
                {
                 'id' : post['id'],
                 'title' : post['title'],
                 'body' : post['body']
                }
                for post in posts
            ]

    with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
          writer = csv.DictWriter(csvfile, fieldnames=['id', 'title', 'body'])
          writer.writeheader()
          writer.writerow({'id': 1, 'title': 'example', 'body': 'text'})
