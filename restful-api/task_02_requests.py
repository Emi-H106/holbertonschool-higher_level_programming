#!/usr/bin/env python3


import requests
import csv


def fetch_and_print_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("Status Code:{}".format(response.status_code))
    if response.status_code == 200:
          posts = response.json()
          for post in posts:
            print(post['title'])

def fetch_and_save_posts():
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
