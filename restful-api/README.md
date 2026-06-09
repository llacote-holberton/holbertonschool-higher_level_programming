# Overview

This repository will hold exercises related to the creation and use of APIs.


# Project informations

<details>
<summary>Embed from https://intranet.hbtn.io/projects/3111</summary>
In the evolving world of software development, understanding how to communicate and transfer data efficiently between systems is essential. This project delves into the domain of RESTful APIs, a cornerstone in the realm of web services. The Representational State Transfer (REST) architecture is a set of constraints that ensure a scalable, stateless, and cacheable communication system. This approach allows for the easy integration of web services, making them accessible to a wide range of applications.

### Learning Objectives:

1. **HTTP/HTTPS Basics**: Grasp the foundational principles of the web&#39;s primary protocol, understanding how data transfer occurs, methods involved, and the difference between the secure and non-secure versions.

2. **API Consumption with Command Line**: Hands-on experience in interacting with APIs using basic command-line tools, laying the groundwork for more advanced interactions.

3. **API Consumption with Python**: Elevate your data fetching skills by leveraging Python&#39;s capabilities, allowing for more advanced processing and data manipulation.

4. **API Development with http.server**: Understand the basics of crafting an API from scratch using Python&#39;s built-in modules, setting a solid foundation.

5. **API Development with Flask**: Dive deeper into API development using the lightweight Flask framework, focusing on routing, data management, and scalability.

6. **API Security &amp; Authentication**: Address the crucial aspect of security, understanding how to protect data transfer and ensure only authorized access to resources.

7. **API Standards &amp; Documentation with OpenAPI**: Conclude with the importance of maintaining standardized documentation, ensuring that APIs are usable, understandable, and maintainable.

### Importance:

In our interconnected digital age, RESTful APIs play a pivotal role in the integration of different systems. They serve as the middlemen, translating requests into understandable actions, fetching data, or triggering procedures. From social media platforms sharing data with advertisement agencies to complex industrial systems communicating with each other for automation, APIs are ubiquitous.

Developing a solid understanding of how to consume, develop, secure, and document these APIs equips you with a critical skill set. It&#39;s a blend of understanding both the technical intricacies and the larger design picture, ensuring seamless and efficient communication in the digital world.

### REST API Conceptual Diagram:

```
+-------+           +-------+           +---------+           +---------+
|       |  Request  |       |  Process  |         |  Fetch/   |         |
|       |   -----&gt;  |       |  -------&gt; |         |  Modify   |         |
|       |           |       |           |         |  -------&gt; |         |
|       | &lt;-----    |       | &lt;-------  |         |           |         |
|       |  Response |       |  Return   |         |           |         |
+-------+           +-------+           +---------+           +---------+
  Client            Web Server           API Server           Database
```

**Components**:

1. **Client**: The requester of the service, often a web browser or application.
2. **Web Server**: Handles the incoming request, acts as a middleman before passing it to the API server.
3. **API Server**: The actual logic layer that processes the request, determining what data or action is required.
4. **Database**: Stores the data which the API might fetch or modify.

**Flow**:

1. The client sends an HTTP/HTTPS request to the Web Server.
2. The Web Server, after potential routing and load balancing, forwards the request to the API Server.
3. The API Server processes the request, interacts with the database if needed.
4. The API Server returns the processed response to the Web Server.
5. The Web Server sends back the final HTTP/HTTPS response to the client.

This diagram provides a high-level view of how RESTful API communication typically works. In simpler setups, the Web Server and API Server might be combined into one. The separation here illustrates potential layers in a more complex or scaled environment.

### Requirements

&gt; IMPORTANT: Your scripts will be tested with Python 3.9.

</details>

# General Rules
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- Your files will be executed with `MySQLdb` version `2.0.x`
- Your files will be executed with `SQLAlchemy` version `1.4.x`
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39; `)
- All your classes should have a documentation (`python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.__doc__)&#39; `)
- All your functions (inside and outside a class) should have a documentation (`python3 -c &#39;print(__import__(&quot;my_module&quot;).my_function.__doc__)&#39; ` and `python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.my_function.__doc__)&#39; `)
- A documentation is not a simple word, it&#39;s a real sentence explaining what&#39;s the purpose of the module, class or method (the length of it will be verified)
- You are not allowed to use `execute` with sqlalchemy

# Exercises

| Task name                                                           | Filename                                       |
|---------------------------------------------------------------------|------------------------------------------------|
| 0. Basics of HTTP/HTTPS                                             | task_00_http-basics_memo.md                    |
| 1. Consume data from an API using command line tools (curl)         | task_01_API-consumption_memo.md                |
| 2. Consuming and processing data from an API using Python           | task_02_requests.py                            |
| 3. Develop a simple API using Python with the `http.server` module  | task_03_http_server.py                         |
| 4. Develop a Simple API using Python with Flask                     | task_04_flask.py                               |
| 5. API Security and Authentication Techniques                       | task_05_basic_security.py                      |

# Resources

The following are recommended resources and tools

## General HTTP documentation

- https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview
- https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

## Curl
- https://ec.haxx.se/
- https://thevalleyofcode.com/lesson/http/http-curl/

## APIs in Python
- https://docs.python-requests.org/en/latest/
- https://docs.python.org/3/library/http.server.html
- https://flask.palletsprojects.com/en/stable/
- https://flask-httpauth.readthedocs.io/en/latest/
- https://flask-jwt-extended.readthedocs.io/en/stable/
- https://www.jwt.io/introduction#what-is-json-web-token

## Tools

- https://jsonplaceholder.typicode.com/ (JSON mockup tool)
