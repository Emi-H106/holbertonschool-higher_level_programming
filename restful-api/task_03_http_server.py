#!/usr/bin/env python3


from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """
     A simple HTTP request handler class for
     demonstrating basic API functionality.
    """
    def do_GET(self):
        """
        Handle GET requests.
        This method checks the request path and serves appropriate responses.
        """
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == '/data':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())
        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        elif self.path == '/info':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info = {
                    "version": "1.0",
                    "description": "A simple API built with http.server"
                    }
            self.wfile.write(json.dumps(info).encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")



def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    """
    Run the HTTP server
    This function initializes and starts
    the HTTP server on the specified port.
    """
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}...')
    httpd.serve_forever()


if __name__ == "__main__":
    run()
