from http.server import BaseHTTPRequestHandler
import time

class handler(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header("Content-Type", "text/plain")
    self.end_headers()
    
    response = str(time.time()).replace('.', '')
    self.wfile.write(response.encode())
    return

