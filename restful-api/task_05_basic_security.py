#!/usr/bin/python3
"""Module experimenting with Requests extension"""

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


if __name__ == "__main__":
    print("\n=== @dev: print users ===\n", users, "\n=== end ===\n", sep="\n")
    app.run()
