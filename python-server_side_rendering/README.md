# Overview

This folder will hold exercises related to server side rendering using Python libraries.

Server-side rendering is a powerful technique where web pages are generated on the server and sent to the client as fully formed HTML. This contrasts with client-side rendering, where the browser builds the web page using JavaScript and dynamic data. Through this project, you will learn how to implement SSR using Python and Flask, leveraging the Jinja templating engine to create dynamic, efficient, and SEO-friendly web applications.

## Learning Objectives

- Understand the concepts of server-side rendering and how it differs from client-side rendering.
- Learn the benefits of using server-side rendering in web development.
- Implement SSR in Python using the Flask framework.
- Utilize Jinja templating engine to dynamically generate HTML pages.
- Read and display data from various sources including JSON, CSV, and SQLite databases.
- Handle dynamic content and user inputs in web applications.

## What to Expect

In this project, you will build a Flask application that serves web pages using server-side rendering techniques. You will start by creating basic templates and gradually move towards integrating dynamic content from multiple data sources. By the end of the project, you will have a comprehensive understanding of SSR, templating, and how to build efficient, scalable web applications.
Resources



This project will equip you with the skills needed to implement server-side rendering in your web applications, making them more efficient, SEO-friendly, and easy to maintain.
## Requirements

### General

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on Ubuntu 20.04 LTS using `node` (version 14.x)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/node`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should be `semistandard` compliant (version 16.x.x). [Rules of Standard](/rltoken/Wz4slq1c0LivUbiR88Kj_Q) + [semicolons on top](/rltoken/n6FW86eM_laCRYFfuHKjXA). Also as reference: [AirBnB style](/rltoken/7O__u3p-BU24HUBUh7QXoQ)
- All your files must be executable
- The length of your files will be tested using `wc`

## More Info

### Install Node 14

```
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

### Install semi-standard

[Documentation](/rltoken/n6FW86eM_laCRYFfuHKjXA)

```
$ sudo npm install semistandard --global
```

# Exercises

| Task name                                                           | Filename                        |
|---------------------------------------------------------------------|---------------------------------|
| 0. Creating a Simple Templating Program                             | task_00_intro.py                |
| 1. Creating a Basic HTML Template in Flask                          | task_01_jinja.py                |
| 2. Creating a Dynamic Template with Loops and Conditions in Flask   | task_02_logic.py                |
| 3. Displaying Data from JSON or CSV Files in Flask                  | task_03_files.py                |
| 4. Extending Dynamic Data Display to Include SQLite in Flask        | task_04_db.py                   |


# Resources

The following are recommended resources and tools

## Documentation

- **MDN Web Docs on Server-Side Web Development:** [MDN Server-Side Web Development](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side)
- **Client-side vs. Server-side vs. Pre-rendering for Web Apps:** [Templating Engines in Web Development](https://www.toptal.com/developers/front-end/client-side-vs-server-side-pre-rendering)
- **Flask Documentation:** [Flask Official Documentation](https://flask.palletsprojects.com/en/stable/)
- **Python JSON Documentation:** [Python JSON Documentation](https://docs.python.org/3/library/json.html)
- **Python CSV Documentation:** [Python CSV Documentation](https://docs.python.org/3/library/csv.html)
- **Python SQLite Documentation:** [Python SQLite Documentation](https://docs.python.org/3/library/sqlite3.html)
- **Jinja2 Documentation:** [Jinja2 Documentation](https://jinja.palletsprojects.com/en/latest/)
