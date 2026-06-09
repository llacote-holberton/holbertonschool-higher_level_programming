#!/usr/bin/python3
"""Module experimenting with AUTH security management"""

from flask import Flask    # Required to set up a webapp
from flask import jsonify  # Required for simple json manipulation
from flask import request  # Required for POST requests to login and get token.
# Importing several utilities as "in-domain functions" for practicity
# JWT = Json Web Token, encrypted string of 3 things: header.payload.signature
from flask_jwt_extended import create_access_token  # JWT Session generator
from flask_jwt_extended import get_jwt_identity     # Decodes payload in JWT
from flask_jwt_extended import jwt_required         # Decorator to impose auth.
from flask_jwt_extended import JWTManager
# Werkzeug (German) stands for "work tools" library of tools for webapps
#   designed in respect of Web Server Gateway Interface convention.
# https://werkzeug.palletsprojects.com/en/stable/utils/
#    #module-werkzeug.security (freaking FINALLY a decent doc!!)
from werkzeug.security import generate_password_hash  # Encrypts strings
from werkzeug.security import check_password_hash     # "Mirror" method

# Custom module externalizing users's registry for readability/maintainability.
from task_05_users_registry import users

# Creating our Flask app, providing script name for simplicity.
app = Flask(__name__)
# Adding a config parameter later used as a "secret part" for our hashes.
# Technically we just add a random new key in the "config" attribute dictionary
#   but we "know" as devs the name must be this for that config to be usable
#   by the actual code of flask_jwt_extension.
app.config["JWT_SECRET_KEY"] = "Python docs suck in general but JWT is worse!"
# In a real project would be an environment variable injected at runtime
# so a) unique per environment (simple for local/isolated, strong for prod)
#    b) not stored in Git or the like nor readable easily.


def _user_exists(username: str) -> bool:
    return any(u.get('username') == username for u in users.values())


def _password_matches(username: str, password: str) -> bool:
    # This time we know all content of our users registry
    #   so here exceptionally we just assume "key == username"
    stored_password_hash = users[username].get('password')
    # print(stored_password)
    # print(generate_password_hash(password))
    # Ends up with different hashs, but no problem as the salt is
    #   publicly stored inside each why is why library reuse it to
    #   make comparisons with provided "raw" strings.
    return check_password_hash(stored_password_hash, password)
    # Which is why the function MUST have a hash in first argument, and a
    #   "plain" password as second, so it can hash it with the same salt and
    #   see if the resulting temporary hash is 100% identical.


def _is_admin(username: str) -> bool:
    # Same as above: we assume key == username AND role has only one str value.
    # We also assume the "user exists" check has been made beforehand!
    return users[username].get('role') == "admin"


@app.route('/')
def homepage():
    return "Welcome on my mini-simulation of Auth management"


if __name__ == "__main__":
    print("\n=== @dev: print users ===\n", users, "\n=== end ===\n", sep="\n")
    app.run()

    def test_basic():
        print("'toto' exists? Expected False, got: ", _user_exists("toto"))
        print("'admin_secondary' (True)? ", _user_exists("admin_secondary"))
        print(_password_matches("admin_secondary", "adminpass2"))
        print(_is_admin("admin_secondary"))
        print(_is_admin("writer_alice"))
