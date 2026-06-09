# Task 01 Overview

<details>
<summary>
  Details from https://intranet.hbtn.io/projects/3111
</summary>

`curl` (Client URL) is a command-line tool that allows users to transfer data to or from a network server, using one of the supported protocols (HTTP, HTTPS, FTP, and more). It&#39;s widely used for debugging, testing, and interacting with RESTful web services and APIs. By mastering `curl`, one can quickly prototype API requests, diagnose server issues, and more, all from the command line.

---

#### Objective:
At the end of this exercise, students should be able to:

1. Install and use `curl` from the command line.
2. Construct and execute basic API requests using `curl`, including setting headers and inspecting the output.
3. Interpret the results of common API requests.

---

#### Resources:
1. [curl - Everything curl](/rltoken/eFoZ3X1pF42IdfyzLC3M3A)
2. [Using cURL to interact with HTTP APIs](/rltoken/AnZ0EuwAm5VSxXAZDygP1g)
3. Public API to play with: [JSONPlaceholder](/rltoken/Ut3d3Tzd0l_sH0evg3GiMg)

---

#### Instructions:

1. **Installing and Basic Interaction with `curl`**:
    - Install `curl` on your system. It&#39;s usually available in standard repositories for Linux/Mac systems. For Windows, consider using Windows Subsystem for Linux (WSL) or downloading a Windows version of `curl`.
    - Once installed, run `curl --version` to confirm its availability.
    - Use `curl` to fetch the content of a webpage. For instance: `curl http://example.com`.

2. **Fetching Data from an API**:
    - Use `curl` to retrieve posts from JSONPlaceholder: `curl https://jsonplaceholder.typicode.com/posts`
    - Observe the output. It should be a JSON array of posts.

3. **Using Headers and Other Options with `curl`**:
    - Fetch only the headers of the same request using `curl -I https://jsonplaceholder.typicode.com/posts`.
    - Use `curl` to make a POST request to the same API: `curl -X POST -d &quot;title=foo&amp;body=bar&amp;userId=1&quot; https://jsonplaceholder.typicode.com/posts`

---

#### Hints:

1. The `-I` flag in `curl` fetches only the headers of the response, which can be useful to diagnose server settings, cache controls, content type, and more.
2. With the `-X` flag, you can specify an HTTP method for your request. For example, `-X POST` will make a POST request.
3. The `-d` flag allows you to pass data in your request. In RESTful APIs, this is commonly used with POST, PUT, or PATCH requests to send data to the server.
4. If you&#39;re getting a lot of output and want to view it in a more organized way, consider piping the output to a tool like `jq` for JSON formatting and highlighting.

---

#### Expected Output:

1. Upon running `curl --version`, you should see details about your installed version of `curl`, including supported protocols.
2. Fetching posts from JSONPlaceholder should provide a JSON output of various posts, each having attributes like `userId`, `id`, `title`, and `body`.
3. Fetching only headers should give a concise output showing status codes and headers without the actual content.
4. Making a POST request should yield a response from the server acknowledging the reception of the data. For JSONPlaceholder, it typically returns the created post with an `id` of `101` (since it doesn&#39;t actually save the new post, but simulates the creation).</div></div>

</details>

## Interesting tips

Curl can fetch multiple resources at once since it's a command line tool so can be combined with globbing.
ex curl https://myblog/202[0-6]/[01-12].html

-v gives details on request/response.
-O option directly saves to disk with same filename.
-u can provide username & password.

## Additional resources
- https://medium.com/@e3x3e/top-5-practical-uses-of-curl-every-engineer-should-know-773207b90006
- https://reqbin.com/req/curl/c-s3bfyrby/curl-examples

