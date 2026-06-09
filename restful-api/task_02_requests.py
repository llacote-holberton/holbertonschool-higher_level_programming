#!/usr/bin/python3
"""Module experimenting with Requests extension"""

import requests
import csv


def fetch_and_print_posts():
    """Displays posts titles from jsonplaceholder stub"""
    # We know by design that the url will return a body of JSON string
    source_url = "https://jsonplaceholder.typicode.com/posts"
    # If all goes well returns a Response object with HTTP code 200
    blog_posts_request = requests.get(source_url)
    # print(dir(blog_posts_json))
    # Response seems iterable (_next + iter ?) and comparable (eq/le/lt)
    # Has important attributes: url, status_code, request.
    # Text is attribute returning raw content, json is method returning dict
    # print(blog_posts_json.text)
    return_code = blog_posts_request.status_code
    if return_code == 200:
        print("Status Code:", return_code)
        for post in blog_posts_request.json():
            print(post['title'])


def fetch_and_save_posts():
    """Saves posts inside a comma structured text file"""
    source_url = "https://jsonplaceholder.typicode.com/posts"
    blog_posts_request = requests.get(source_url)
    return_code = blog_posts_request.status_code
    csv_filename = "posts.csv"

    if return_code == 200:
        try:
            posts_list = blog_posts_request.json()
            with open(csv_filename, 'w') as csv_file:
                csv_headers = ['id', 'title', 'body']
                # NOTE: writer NEEDS an opened string stream hence why
                #   initiated inside the "with open"
                # https://docs.python.org/3/library/csv.html#csv.DictWriter
                writer = csv.DictWriter(
                    csv_file,
                    # WARNING: header names MUST match keys in value items.
                    fieldnames=csv_headers,
                    # "Magic" option making writer automatically ignore extra
                    #   "columns" from value rows which don't match headers
                    extrasaction='ignore'
                )
                writer.writeheader()
                for post in posts_list:
                    writer.writerow(post)
        except PermissionError as e:
            print(f"Insufficient permission to open file {csv_filename}")
        except FileNotFound as e:
            print(f"File {csv_filename} not found")
        except OSError as e:
            print(f"Error when manipulating file {csv_filename}")
