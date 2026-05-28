from os import getenv
from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(getenv('RESPONSE-TEXT').encode('utf-8'))

if __name__ == "__main__":
    with HTTPServer(('0.0.0.0', 8080), Handler) as server:
        server.serve_forever()