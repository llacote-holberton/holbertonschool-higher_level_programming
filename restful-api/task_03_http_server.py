#!/usr/bin/python3
"""Module experimenting with Requests extension"""

# Required to create custom server
from http.server import HTTPServer, BaseHTTPRequestHandler
import json  # In case of
import html  # Required to sanitize user input


# Confer https://koor.fr/Python/API/python/
#                wsgiref.simple_server/BaseHTTPRequestHandler/Index.wp
class PeopleDataHandler(BaseHTTPRequestHandler):
    """Simple API to manipulate basic people's metadatas"""
    server_info = {"version": "1.0",
                   "description": "A simple API built with http.server"}
    sample_data = {"name": "John", "age": 30, "city": "New York"}

    def health_check(self):
        """Pings back server is working"""
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write("OK".encode('utf-8'))

    def homepage(self):
        """Handle the homepage"""
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        welcome_message = """
            <html>
                <body>
                    Hello, this is a simple API!
                </body>
            </html>
        """
        self.wfile.write(welcome_message.encode('utf-8'))

    def error_404(self):
        self.send_response(404)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        sanitized_url = html.escape(self.path)
        err_msg = "<html><body>Sorry, requested url {} not found</body></html>"
        self.wfile.write(err_msg.format(sanitized_url).encode('utf-8'))

    def page__data(self):
        self.send_response(200)  # Code for "all ok"
        # HEADERS (for now we just define one)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        # BODY using "file-like" object attached to the class as attribute.
        # Doesn't work as is, write expects BYTES, json provides STRING
        # self.wfile.write(json.dumps(self.sample_data))
        self.wfile.write(json.dumps(self.sample_data).encode('utf-8'))

    def page__info(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(self.server_info).encode('utf-8'))

    def do_GET(self):
        if self.path == '/':
            self.homepage()
        elif self.path == '/status':
            self.health_check()
        elif self.path == '/info':
            self.page__info()
        elif self.path == '/data':
            self.page__data()
        else:
            self.error_404()


# Choice to use subclass to encapsulate configuration
# Confer https://koor.fr/Python/API/python/
#                wsgiref.simple_server/HTTPServer/Index.wp
class PeopleApiServer(HTTPServer):
    # Config parameters put on the fly in subclass init
    #   to "feed" the regular init of the parent class.
    def __init__(self):
        host = "localhost"
        port = 8000
        super().__init__((host, port), PeopleDataHandler)


def run_server():
    demo_api = PeopleApiServer()
    # Method which opens an infinite loop for server to listen on requests.
    demo_api.serve_forever()


if __name__ == "__main__":
    # print(dir(PeopleDataHandler))
    # help(PeopleDataHandler)
    run_server()
