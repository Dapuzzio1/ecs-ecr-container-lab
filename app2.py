import os
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = int(os.environ.get("PORT", 9090))

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(f"Hello from app on port {PORT}\n".encode())

if __name__ == "__main__":
    server = HTTPServer(("", PORT), SimpleHandler)
    print(f"Starting server on port {PORT}")
    server.serve_forever()

