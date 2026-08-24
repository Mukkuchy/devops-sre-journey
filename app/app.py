<<<<<<< HEAD

---

## app/app.py

```python
=======
>>>>>>> 8c542fd (Day 1: Linux basics and project setup)
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/health':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "UP"}).encode())
        elif self.path == '/api/v1/message':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"message": "Hello from QA to DevOps"}).encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'{"error": "Not Found"}')

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 5000), Handler)
    print('Server running on port 5000...')
    server.serve_forever()
