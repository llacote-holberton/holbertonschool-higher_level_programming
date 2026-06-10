#!/usr/bin/python3
"""Module testing quality of auth management"""
import requests                           # Used to make test requests
from task_05_users_registry import users  # Used to automate tests on all users

server_url = "http://localhost:5000"      # Global var for tests consistency

def test_home():
    homepage = requests.get(f"{server_url}/")
    print(homepage)


def test_login_with_autoheader():
    lolo__response = requests.get(
        f"{server_url}/basic-protected",
        # tuple (username, password)
        auth=("lolo", "1234456")
    )
    print(lolo__response)

    user_standard__response = requests.get(
        f"{server_url}/basic-protected",
        auth=("user_standard", "password123")
        # Generates the Authorization: Basic header
    )
    print(user_standard__response)


def test_get_jwt_for_valid(user):


    valid_name = user.get('username')
    valid_pwd = user.get('raw_pwd')
    print(f"@dev REQUEST: JWT for user '{valid_name}' / pwd '{valid_pwd}'")
    # Using POST per endpoint requirements
    valid_req_return = requests.post(
        f"{server_url}/login",
        # Providing a dict for json param since JSON expected by endpoint
        json={"username": valid_name, "password": valid_pwd}
    )
    code = valid_req_return.status_code
    token = valid_req_return.json()["access_token"]
    print(f"@dev RESULT: status {code}, token value...\n {token}\n")

def test_get_jwt_for_inexisting_user():

    inexisting = "Nemo"
    pwd = "hidden"
    print(f"@dev REQUEST: JWT for inexisting usr '{inexisting}' / pwd '{pwd}'")
    response = requests.post(
        f"{server_url}/login",
        json={"username": inexisting, "password": pwd}
    )
    print(f"@dev RESULT: {response.status_code}, msg {response.json()}\n")

def test_get_jwt_with_wrong_password():
    valid_name = users['user_standard'].get('username')
    valid_pwd = users['user_standard'].get('raw_pwd')
    wrong_pwd = valid_pwd + 'THIS IS WRONG!'
    print(wrong_pwd)
    print(f"@dev REQUEST: JWT for usr '{valid_name}' with pwd {wrong_pwd}")
    response = requests.post(
        f"{server_url}/login",
        json={"username": valid_name, "password": wrong_pwd}
    )
    print(f"@dev RESULT: {response.status_code}, msg {response.json()}\n")


if __name__ == "__main__":
    print("======= START Auth API TESTS ========")
    test_home()
    test_login_with_autoheader()

    print("=== @dev Testing JWT retrieval for VALID users ===")
    for user in users:
        test_get_jwt_for_valid(users.get(user))

    print("=== @dev Testing JWT retrieval for INEXISTING user ===")
    test_get_jwt_for_inexisting_user()

    print("=== @dev Testing JWT retrieval for 1st user with wrong pwd ===")
    test_get_jwt_with_wrong_password()

















