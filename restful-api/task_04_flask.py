#!/usr/bin/python3
"""Module experimenting with Requests extension"""

from flask import Flask    # Required to set up a webapp
from flask import jsonify  # Required for simple json manipulation
from flask import request  # Required for POST requests to add/alter data

# Example dictionary
users = {
    # "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "LA"},
    # "john": {"username": "john", "name": "John", "age": 30, "city": "NY"}
}

app = Flask(__name__)


# Decorator "root" must match the instance of Flask (here 'app')
#   AND the instance must (logically) be created BEFORE ALL
#   "router method" decorators.
@app.route("/")
def home():
    """Returns HTML-formatted welcome message"""
    return "Welcome to the Flask API!"


@app.route("/status")
def health_check():
    """Signals server is up and running"""
    return "OK"


@app.route("/data")
def send_users_data():
    """Returns JSON-formatted data on known users"""
    # Task requires a plain list of all the usernames of the registry.
    # Although from sample data we could consider that username = key,
    # I prefer going for the robust & explicit method.
    # Using the "list comprehension" syntax
    # REMINDER!! Dict =/= list, must get a list of its values
    # usernames = [username for user in users]
    usernames = [u['username'] for u in users.values()]
    return jsonify(usernames)


def _user_exists(username: str) -> bool:
    "Helper: checks if string matches at least one 'username' data in registry"
    return any(u.get('username') == username for u in users.values())


@app.route('/user/<string:username>')
def show_user_data(username):
    """Returns all data for given username if exist"""
    # Using "any" syntax wouldn't work as the "context" is lost
    #   as soon as it stops, it only returns True/False
    # {if any(
    #     u.get('username') == username
    #     for u in users.values()
    # ):
    #     return jsonify(u)
    # So time for an old for loop because as above
    # I have no guarantee that dict key will always match username
    user_found = None
    for u in users.values():
        if u.get('username') == username:
            user_found = u
            break
    if user_found is None:
        msg__notfound = {"error": "User not found"}
        # Flask expects specific HTTP code to come as second argument of return
        return jsonify(msg__notfound), 404
    else:
        return jsonify(user_found)


@app.route('/add_user', methods=['POST'])
def insert_new_user():
    """Adds a user in registry if valid data provided"""

    # Defining the responses for different "use-cases"
    error_response__invalid_json = ({"error": "Invalid JSON"}, 400)
    error_response__missing_username = ({"error": "Username is required"}, 400)
    error_response__user_exists = ({"error": "Username already exists"}, 409)
    # request is a "local proxy", one Request instance among many
    #   which Flask associate to a unique Thread for a given HTTP request.
    # So it automatically has the "right context"
    # received_data = request.get_json()
    # Option automatically rejects malformed JSON and returns None instead.
    received_data = request.get_json(silent=True)
    if received_data is None:
        return error_response__invalid_json
    # Get is the safe way to try and access a key in dict
    new_username = received_data.get("username")
    if new_username is None:
        return error_response__missing_username
    if _user_exists(new_username):
        return error_response__user_exists
    users[new_username] = received_data
    success_message = {"message": "User added", "user": received_data}
    return (jsonify(success_message), 201)


""" TO TEST route with Curl...
 curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"username":"xyz","name":"Ryo Saeba", "age": 34, "city": "Tokyo"}' \
  http://localhost:5000/add_user
"""


if __name__ == "__main__":
    app.run()
