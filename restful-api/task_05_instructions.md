# Official task description

Grabbed from https://intranet.hbtn.io/projects/3111?task_index=5

API security is of paramount importance, especially when the API is exposed to the wider internet. There are many risks, including unauthorized data access, data tampering, and denial-of-service attacks. One fundamental method of securing APIs is to use authentication and authorization mechanisms, ensuring only authorized users can access certain resources.

---

#### Objective:
At the end of this exercise, students should be able to:

1. Understand the importance of API security.
2. Implement basic authentication using Flask.
3. Set up token-based authentication with JSON Web Tokens (JWT).
4. Differentiate between authentication and authorization.

---

#### Resources:
1. [Flask-HTTPAuth](/rltoken/88vjjCBJYisW22vWIm1p4A)
2. [Flask-JWT-Extended](/rltoken/-KgyiHhniaqRQMh7WRIItA)
3. [Introduction to JSON Web Tokens](/rltoken/UOJ__DgwD0OtPKgy_Ox-Pg)

---

#### Instructions:

##### Basic Authentication:

1. **Install Flask-HTTPAuth**:
   - Run: `pip install Flask-HTTPAuth`.

2. **Set up Basic HTTP Authentication**:
   - Create a list of users and their hashed passwords.
   - Use the `werkzeug.security` library for password hashing and verification.

3. **Protect Routes with Basic Authentication**:
   - Use the `@auth.login_required` decorator to protect certain routes.

##### Token-based Authentication with JWT:

1. **Install Flask-JWT-Extended**:
   - Run: `pip install Flask-JWT-Extended`.

2. **Set up JWT-based Authentication**:
   - Use a secret key for token generation and validation.
   - Create a route `/login` where users can log in with their credentials and receive a JWT token.

3. **Protect Routes with JWT Tokens**:
   - Use the `@jwt_required()` decorator to protect certain routes.

4. **Implement Role-based Access Control**:
   - Add roles (e.g., `admin`, `user`) to your users.
   - Create routes that should only be accessible to certain roles.
   - Implement checks to ensure the user&#39;s role matches the required role for accessing specific routes.

---

##### Hints:

- For basic authentication, store passwords securely using `werkzeug.security.generate_password_hash` and verify them using `werkzeug.security.check_password_hash`.
- Embed user information, such as roles, within the JWT token payload.
- Use a strong secret key for JWT token generation and validation.
- Utilize `get_jwt_identity()` to retrieve user information from the current JWT token.

---

#### API Specifications:

##### User Data:

- Users should be stored in memory using a dictionary with the following structure:
 
  ```python
users = {
    &quot;user1&quot;: {&quot;username&quot;: &quot;user1&quot;, &quot;password&quot;: generate_password_hash(&quot;password&quot;), &quot;role&quot;: &quot;user&quot;},
    &quot;admin1&quot;: {&quot;username&quot;: &quot;admin1&quot;, &quot;password&quot;: generate_password_hash(&quot;password&quot;), &quot;role&quot;: &quot;admin&quot;}
}
  ```

##### Endpoints:

1. **Basic Authentication**:

   - **Protected Route**:
     - URL: `/basic-protected`
     - Method: `GET`
     - Description: Returns a message `&quot;Basic Auth: Access Granted&quot;` if the user provides valid basic authentication credentials.
     - Authentication: Basic

2. **JWT Authentication**:

   - **Login**:
     - URL: `/login`
     - Method: `POST`
     - Description: Accepts JSON payload with `username` and `password`. Returns a JWT token if credentials are valid.
     - Example Request:
     
       ```json
       {
           &quot;username&quot;: &quot;user1&quot;,
           &quot;password&quot;: &quot;password&quot;
       }
       ```
			 
     - Example Response:
     
       ```json
       {
           &quot;access_token&quot;: &quot;&lt;JWT_TOKEN&gt;&quot;
       }
       ```

   - **JWT Protected Route**:
     - URL: `/jwt-protected`
     - Method: `GET`
     - Description: Returns a message `&quot;JWT Auth: Access Granted&quot;` if the user provides a valid JWT token.
     - Authentication: JWT

   - **Role-based Protected Route**:
     - URL: `/admin-only`
     - Method: `GET`
     - Description: Returns a message `&quot;Admin Access: Granted&quot;` if the user is an admin.
     - Authentication: JWT with role check

##### Expected Output:

1. Accessing `/basic-protected` without credentials should return a `401 Unauthorized` response.
2. Accessing `/basic-protected` with valid credentials should return `&quot;Basic Auth: Access Granted&quot;`.
3. Posting valid credentials to `/login` should return a JWT token.
4. Accessing `/jwt-protected` without a token or with an invalid token should return a `401 Unauthorized` response.
5. Accessing `/jwt-protected` with a valid token should return `&quot;JWT Auth: Access Granted&quot;`.
6. Accessing `/admin-only` with a non-admin token should return a `403 Forbidden` response `{&quot;error&quot;: &quot;Admin access required&quot;}`.
7. Accessing `/admin-only` with an admin token should return `&quot;Admin Access: Granted&quot;`.

#### Important Note:

When implementing authentication in your Flask API, ensure that all authentication errors return a `401 Unauthorized response`. This includes errors due to missing, invalid, expired, or malformed tokens. Returning a consistent `401` status code for authentication errors is crucial for passing the automated tests. Failure to return a `401` status code for these errors may result in failing tests.

#### Hints:

- **Custom Error Handlers**: Use `Flask-JWT-Extended`&#39;s decorators to create custom error handlers for different types of JWT errors. 

Here are some examples:

  ```python
  from flask_jwt_extended import JWTManager

  app = Flask(__name__)
  jwt = JWTManager(app)

  @jwt.unauthorized_loader
  def handle_unauthorized_error(err):
      return jsonify({&quot;error&quot;: &quot;Missing or invalid token&quot;}), 401

  @jwt.invalid_token_loader
  def handle_invalid_token_error(err):
      return jsonify({&quot;error&quot;: &quot;Invalid token&quot;}), 401

  @jwt.expired_token_loader
  def handle_expired_token_error(err):
      return jsonify({&quot;error&quot;: &quot;Token has expired&quot;}), 401

  @jwt.revoked_token_loader
  def handle_revoked_token_error(err):
      return jsonify({&quot;error&quot;: &quot;Token has been revoked&quot;}), 401

  @jwt.needs_fresh_token_loader
  def handle_needs_fresh_token_error(err):
      return jsonify({&quot;error&quot;: &quot;Fresh token required&quot;}), 401
  ```
