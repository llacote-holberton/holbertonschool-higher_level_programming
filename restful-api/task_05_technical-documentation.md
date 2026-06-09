
# Project overview

This app is a web app using Flask to expose an HTTP server able to answer requests on different endpoints.
It aims at simulating the "authentification" aspect which is primordial in many webapps as a prerequisite
  to ensure security of data and processes and restrict CRUD permissions to people with adequate habilitations.

For details about "business requirements" and pedagogical goals please confer task_05_instructions.md file.

# How to run

1. Ensure you have Python3 >=3.9 installed as well as the following extensions/libraries in compatible versions
   * Flask (pip install Flask)
   * Flask Auth (pip install Flask-HTTPAuth)
   * Flask JWT Extended (pip install Flask-JWT-Extended)
   * Werkzeug (pip install Werkzeug)

2. In a Command Line Interface, run `python3 task_05_basic_security.py`


# Functional behaviour

## Web exposition

App uses the default port from Flask and run without specific domain, aka is exposed only internally at url "https://localhost:5000".

## Routes

| Route name        | Method  | Authent? | Role(s) | Case             | Success message                     |
|-------------------|---------|----------|---------|------------------|-------------------------------------|
| / (extra)         | GET     | None     | *       | Welcome message  | HTML: "Welcome to auth simulator"   |
| /basic-protected  | GET     | Basic    | *       | Tests basic auth | HTML: "Basic Auth: Access Granted"  |
| /login            | POST    | None     | *       | Get JWT token    | JSON: "access_token": "<JWT_TOKEN>" |
| /jwt-protected    | GET     | JWT      | *       | Access backend   | HTML: "JWT Auth: Access Granted"    |
| /admin-only       | GET     | JWT      | admin   | Configure app    | HTML: "Admin Access: Granted"       |


# Technical architecture

NOTE: CRUD operations on users are out of scope of this project apart from the R (Read) one.
Thus why no related function to modify user data or add/delete user.

## Libraries
- Flask: used to expose a REST capable HTTP server.
- JWT: used to protect endpoint access by requiring authentification, "decorates" the Flask app.
- Werkzeug: subparts of that WSGI tools library used to protect sensitive data (passwords, tokens) by hash (non-reversible contrarily to encryption) process.

## Files

- Readonly module "task_05_users_registry" holding a flat, static list of users.
- Main app' code in task_05_basic_security.py

## Functions

### Helper "assertive" functions (returning True/False)
- _user_exists(username) -> to make a first check before doing more intensive ones such as password reading.
- _password_matches(username, password) -> grab user in registry from username, checks password
- _get_jwt_token(username) -> generates a (new) token if need be (may use caching strategy if not too complex).
- _is_admin(username) -> checks user has "admin" role

### Route appaired functions

| Route name        | Func name                          | Authentification infos vector                     |
|-------------------|------------------------------------|---------------------------------------------------|
| / (extra)         | home()                             | None                                              |
| /basic-protected  | user_auth__plain_password_check    | Authorization: Basic <base64("username:password") |
| /login            | user_auth__get_jwt_token           | Body JSON: {"username": "...", "password": "..."} |
| /jwt-protected    | request_restricted_access_with_jwt | Authorization: Bearer <jwt_token_string>          |
| /admin-only       | request_admin_access_with_jwt      | Authorization: Bearer <jwt_token_string>          |



