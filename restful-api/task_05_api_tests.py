#!/usr/bin/python3
"""Module testing quality of auth management"""
import requests


def test_home():
    homepage = requests.get("http://localhost:5000/")
    print(homepage)


def test_login_with_autoheader():
    lolo__response = requests.get(
        "http://localhost:5000/basic-protected",
        # tuple (username, password)
        auth=("lolo", "1234456")
    )
    print(lolo__response)

    user_standard__response = requests.get(
        "http://localhost:5000/basic-protected",
        auth=("user_standard", "password123")
        # Generates the Authorization: Basic header
    )
    print(user_standard__response)


if __name__ == "__main__":
    print("======= START Auth API TESTS ========")
    test_home()
    test_login_with_autoheader()
