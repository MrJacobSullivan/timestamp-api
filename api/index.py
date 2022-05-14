from http.server import BaseHTTPRequestHandler
from urllib import parse
import time

class handler(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header("Content-Type", "text/plain")
    self.end_headers()
    
    response = time.time()
    self.wfile.write(response.encode())
    return

