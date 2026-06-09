# HTTP in three sentences
HTTP is a standard protocol defining how to exchange data on the internet, standing for Hypernet Text Transfer Protocol.
It is designed around a client/server relationship where a client sends a request to a server which returns a response with a code and (case arising) body.
It is stateless (cannot adjust behaviour depending on previous request, no "memory") but has sessions (keeping authentification information to ease multiple exchanges).

# Key differences between HTTP and HTTPS
HTTP has no embedded security, meaning that everything transits without being ciphered. Consequently any attacker can easily use "man-in-the-middle" proxy attacks to sniff and retrieve every sensitive information including bank data, personal accounts and more.

HTTPS stands for -Secured, and adds a layer of security by encrypting the data flow between sender and recipient.
It relies on a public key shared to all potential client devices to ensure that the data can actually be decrypted through a special information set called "SSL certificated".
To ensure the privacy of one-to-one communication client and server generate a new pair of private/public key on top of the previous, unique for the upcoming exchanges (handshake).

## How is the "handshake" established?
1. ClientHello — The browser initiates the handshake by sending the TLS versions it supports, its list of cipher suites, and a random number (client random).
2. ServerHello — The server responds by choosing the TLS version and cipher suite, sending its own random number (server random), and providing its digital certificate (which contains its public key).
3. Certificate Verification — The browser validates the server's certificate: it checks that it was signed by a trusted Certificate Authority (CA), that it hasn't expired, and that it matches the domain being visited.
4. Key Exchange — The two parties establish a shared secret without ever transmitting it directly over the network — either via RSA (the client encrypts a secret with the server's public key) or, more modernly, via ECDHE (Diffie-Hellman, enabling Perfect Forward Secrecy).
5. Session Key Generation — Both sides independently derive the same symmetric session keys (e.g. AES-256) from the two random numbers and the shared secret.
6. Handshake Finished — Each party sends a Finished message encrypted with the session key, confirming the negotiation was successful. The secure connection is now established.

# How are request and response composed?

## HTTP Request Structure

```
METHOD /path HTTP/version
Header-Name: Header-Value
Header-Name: Header-Value
                              ← blank line (mandatory)
Body (optional)
```

**Example:**
```http
POST /api/login HTTP/1.1
Host: example.com
Content-Type: application/json
Authorization: Bearer <token>

{"username": "alice", "password": "1234"}
```

---

## HTTP Response Structure

```
HTTP/version STATUS_CODE Reason-Phrase
Header-Name: Header-Value
Header-Name: Header-Value
                              ← blank line (mandatory)
Body (optional)
```

**Example:**
```http
HTTP/1.1 200 OK
Content-Type: application/json
Set-Cookie: session=abc123

{"message": "Login successful"}
```

---

## Common Status Codes

| Code | Meaning               |
|------|-----------------------|
| 200  | OK                    |
| 201  | Created               |
| 301  | Moved Permanently     |
| 400  | Bad Request           |
| 401  | Unauthorized          |
| 403  | Forbidden             |
| 404  | Not Found             |
| 500  | Internal Server Error |

## List of main HTTP codes with classic use-cases
## HTTP Methods

| Method  | Description                                 | Use Case Example                          |
|---------|---------------------------------------------|-------------------------------------------|
| GET     | Retrieve a resource (read-only, no body)    | Fetch a user profile: `GET /users/42`     |
| POST    | Submit data to create a new resource        | Create an account: `POST /users`          |
| PUT     | Replace a resource entirely                 | Update a full profile: `PUT /users/42`    |
| PATCH   | Partially update a resource                 | Change just an email: `PATCH /users/42`   |
| DELETE  | Remove a resource                           | Delete a post: `DELETE /posts/7`          |
| HEAD    | Same as GET but returns headers only        | Check if a resource exists before fetching|
| OPTIONS | Returns the methods allowed on a resource   | CORS preflight check by the browser       |

---

## HTTP Status Codes

### 1xx — Informational
| Code | Name                | Description                              | Use Case Example                         |
|------|---------------------|------------------------------------------|------------------------------------------|
| 100  | Continue            | Server received headers, client may proceed | Large file upload in two steps        |
| 101  | Switching Protocols | Server agrees to upgrade the protocol   | Upgrading HTTP → WebSocket               |

### 2xx — Success
| Code | Name                | Description                              | Use Case Example                         |
|------|---------------------|------------------------------------------|------------------------------------------|
| 200  | OK                  | Request succeeded                        | `GET /users/42` returns the user         |
| 201  | Created             | Resource successfully created            | `POST /users` after registration         |
| 204  | No Content          | Success but no body to return            | `DELETE /posts/7` after deletion         |

### 3xx — Redirection
| Code | Name                | Description                              | Use Case Example                         |
|------|---------------------|------------------------------------------|------------------------------------------|
| 301  | Moved Permanently   | Resource has a new permanent URL         | HTTP → HTTPS redirect                    |
| 302  | Found               | Temporary redirect to another URL        | Redirect after login                     |
| 304  | Not Modified        | Cached version is still valid            | Browser reuses cached asset              |

### 4xx — Client Errors
| Code | Name                | Description                              | Use Case Example                         |
|------|---------------------|------------------------------------------|------------------------------------------|
| 400  | Bad Request         | Malformed or invalid request syntax      | Missing required field in JSON body      |
| 401  | Unauthorized        | Authentication required or failed        | Accessing an endpoint without a token    |
| 403  | Forbidden           | Authenticated but not permitted          | Regular user accessing an admin route    |
| 404  | Not Found           | Resource does not exist                  | `GET /users/9999` (unknown user)         |
| 405  | Method Not Allowed  | HTTP method not supported on this route  | Sending `DELETE` to a read-only endpoint |
| 409  | Conflict            | State conflict with the current resource | Registering with a




