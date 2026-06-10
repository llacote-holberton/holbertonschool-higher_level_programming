#!/usr/bin/python3
"""Module experimenting with AUTH security management"""

# ==========  0. IMPORTS ==========
from flask import Flask    # Required to set up a webapp
from flask import jsonify  # Required for simple json manipulation
from flask import request  # Required for POST requests to login and get token.
# Importing several utilities as "in-domain functions" for practicity
# JWT = Json Web Token, encrypted string of 3 things: header.payload.signature
from flask_jwt_extended import create_access_token  # JWT Session generator
from flask_jwt_extended import get_jwt_identity     # Decodes payload in JWT
from flask_jwt_extended import get_jwt              # Extracts all JWT infos
from flask_jwt_extended import jwt_required         # Decorator to impose auth.
from flask_jwt_extended import JWTManager
# Werkzeug (German) stands for "work tools" library of tools for webapps
#   designed in respect of Web Server Gateway Interface convention.
# https://werkzeug.palletsprojects.com/en/stable/utils/
#    #module-werkzeug.security (freaking FINALLY a decent doc!!)
from werkzeug.security import generate_password_hash  # Encrypts strings
from werkzeug.security import check_password_hash     # "Mirror" method

from flask_httpauth import HTTPBasicAuth  # Required for "basic auth"

# Custom module externalizing users's registry for readability/maintainability.
from task_05_users_registry import users

# ==========  0. SERVER APP's Config + enabling BasicAuth & JWT-Auth ==========
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

# REQUIRED instanciation to parse the annocations @auth.*
# https://flask-httpauth.readthedocs.io/en/latest/getting-started.html
#                                          #basic-authentication-example
auth = HTTPBasicAuth()

# REQUIRED instanciation EXACTLY LIKE THIS to use the JWT auth system.
jwt = JWTManager(app)


def _user_exists(username: str) -> bool:
    """Checks whether a username exists in the users registry."""
    return any(u.get('username') == username for u in users.values())


def _password_matches(username: str, password: str) -> bool:
    """
    Verifies a plain-text password against the stored hash for a given user.
    Warning: assumes the user exists (call _user_exists beforehand).
    Warning: assumes registry structure where key & username are identical.
    """

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
    """
    Checks whether a given user holds the 'admin' role.
    NOTE: same assumptions as for _password_matches
    AND assumption that role metadata only holds one single string value.
    """
    return users[username].get('role') == "admin"


@auth.verify_password
def verify_password(username, password) -> bool:
    """
    Flask-HTTPAuth callback. Automatically called when a route decorated
    with @auth.login_required receives a request.
    Extracts credentials from the Authorization: Basic header and
    delegates verification to _user_exists and _password_matches.
    """
    if not _user_exists(username):
        return False
    return _password_matches(username, password)


@app.route('/')
def homepage():
    """Returns a plain-text welcome message. No authentication required."""
    return "Welcome on my mini-simulation of Auth management"


@app.route('/basic-protected', methods=["GET"])
def user_auth__plain_password_check():
    """
    GET /basic-protected
    Protected by HTTP Basic Authentication via @auth.login_required.
    Returns a confirmation message if credentials are valid.
    Expected: 200 "Basic Auth: Access Granted"
    """
    access_confirmation = "Basic Auth: Access Granted"
    return access_confirmation


@app.route('/login', methods=["POST"])
def user_auth__get_jwt_token():
    """
    POST /login
    Accepts a JSON payload with 'username' and 'password'.
    Validates credentials against the registry and returns a signed JWT.
    Expected: 200 {"access_token": "<JWT>"} or 401 on invalid credentials.
    """

    # Reminder: request is an object magically instanciated
    #   with the right context by Flask
    username = request.json.get("username", None)
    # Second argument of that get is a fallback value
    password = request.json.get("password", None)
    if username is None or not _user_exists(username):
        return jsonify(msg="Invalid username"), 401
    if not _password_matches(username, password):
        return jsonify(msg="Wrong password"), 401
    # Identity param is mandatory but you can put complex objects in it
    #   as long as it is serialized.
    user_jwt = create_access_token(identity=username)
    return jsonify(access_token=user_jwt)


@app.route('/jwt-protected', methods=["GET"])
# ESSENTIAL! Function body is executed ONLY IF REQUEST HAS VALID JWT
# Otherwise it sends error 422 (by default) immediately.
@jwt_required()
def request_restricted_access_with_jwt():
    """
    GET /jwt-protected
    Protected by @jwt_required(). Grants access to any authenticated user
    regardless of role. Token validation is handled entirely by the decorator.
    Expected: 200 {"access_confirmation": "JWT Auth: Access Granted"}
    """

    # If we get here then by design there is a valid jwt usable in context.
    # Python automagically "extracts" the "identity" and "claims" metadata
    #   from the token provided in Request Headers.
    current_user = get_jwt_identity()
    # Above: useful IF we wanted to use the username contained in the jwt
    return jsonify(access_confirmation="JWT Auth: Access Granted")
    # ONLY WAY to control "error handling" is using specific @jwt.* decorators:
    # invalid_token_loader, expired_token_loader, unauthorized_loader etc


@app.route('/admin-only', methods=["GET"])
@jwt_required()
def request_admin_access_with_jwt():
    """
    GET /admin-only
    Protected by @jwt_required(). Grants access only to users with the 'admin'
    role. Role is verified live against the registry (not from the token)
    to ensure revoked or changed roles are always up to date.
    Expected: 200 on success, 403 {"error": "Admin access required"} otherwise.
    """
    required_role = 'admin'
    msg__access_granted = "Admin Access: Granted"
    msg__access_refused_invalid_role = "Admin access required"
    # Because admin is extra sensitive area
    # Even if it is less performant than the "role in token" approach
    # I prefer just (re)loading all user data from registry and check directly
    #   the roles of currently authenticated user.
    current_username = get_jwt_identity()
    current_user = users[current_username]
    if current_user.get('role') == required_role:
        # Reminder: if nothing specified Flask automagically sets 200 status.
        return jsonify(msg__access_granted)
    else:
        return jsonify(error=msg__access_refused_invalid_role), 403


# ===== EXTRA ROUTES to demonstrate VARIANTS USES of JWT =====
@app.route('/get_jwt_with_role', methods=["POST"])
def user_auth__get_jwt_with_role():
    """
    POST /get_jwt_with_role  [EXTRA]
    Variant of /login that embeds the user's role in the JWT payload
    via additional_claims. Demonstrates the alternative approach where
    authorization info is carried by the token rather than re-fetched
    from the registry on each request.
    Expected: 200 {"access_token": "<JWT>"} or 401 on invalid credentials.
    """
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username is None or not _user_exists(username):
        return jsonify(msg="Invalid username"), 401
    if not _password_matches(username, password):
        return jsonify(msg="Wrong password"), 401

    # THIS TIME we add the "role information" in an "accessory objet" called
    # 'additional_claims' which is designed to hold any contextual info which
    #   may be useful for interactions between authentified user and the app.
    user_jwt_with_role = create_access_token(
        identity=username,
        additional_claims={"role": users[username]["role"]}
    )
    return jsonify(access_token=user_jwt_with_role)


@app.route('/writer-only', methods=["GET"])
@jwt_required()
def request_writer_access_with_jwt_bearing_role():
    """
    GET /writer-only  [EXTRA]
    Protected by @jwt_required(). Grants access only to users whose JWT
    contains a 'role' claim equal to 'writer'. Demonstrates role-based
    access control using additional_claims embedded in the token,
    as opposed to the live registry lookup used in /admin-only.
    Expected: 200 on success, 403 {"error": "Writer role required"} otherwise.
    """
    required_role = 'writer'
    msg__access_granted = "Content Edition Access: Granted"
    msg__access_refused_invalid_role = "Writer role required"

    user_token_infos = get_jwt()
    if user_token_infos.get('role') == 'writer':
        # Reminder: if nothing specified Flask automagically sets 200 status.
        return jsonify(access_granted=msg__access_granted)
    else:
        return jsonify(error=msg__access_refused_invalid_role), 403


# ===== JWT EXCEPTION HANDLERS, using examples provided by task =====
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """JWT error handler: missing or absent token → 401."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """JWT error handler: malformed or tampered token → 401."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """JWT error handler: expired token → 401."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """JWT error handler: explicitly revoked token → 401."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """JWT error handler: route requires a fresh token → 401."""
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    print("\n=== @dev: print users ===\n", users, "\n=== end ===\n", sep="\n")
    app.run()

    def test_basic():
        print("'toto' exists? Expected False, got: ", _user_exists("toto"))
        print("'admin_secondary' (True)? ", _user_exists("admin_secondary"))
        print(_password_matches("admin_secondary", "adminpass2"))
        print(_is_admin("admin_secondary"))
        print(_is_admin("writer_alice"))
