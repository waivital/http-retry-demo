import os
import time

from http.server import HTTPServer, BaseHTTPRequestHandler


shared_file = open('./sharedfile','a')
output_str = "[{}] Hello there -- hostname:{} requid:{} \n"

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

  def do_GET(self):
    index_file = open('./index.html', 'rb')
    if self.path == '/':
      self.send_response(200)
      self.send_header('Content-type', 'text/html')
      self.end_headers()
      html = index_file.read().decode('utf-8').replace('${HOSTNAME}', os.environ.get('HOSTNAME'))
      self.wfile.write(html.encode('utf-8'))
    else:
      self.send_response(404)
      self.end_headers()
    index_file.close()

  def do_POST(self):
    shared_file.write(output_str.format(time.ctime(), os.environ.get('HOSTNAME'), self.headers['X-requid']))
    shared_file.flush()
    time.sleep(2)
    self.send_response(408)
    self.end_headers()
    self.connection.close()


httpd = HTTPServer(('0.0.0.0', 8080), SimpleHTTPRequestHandler)

print('Server starts')

try:
  httpd.serve_forever()
except KeyboardInterrupt:
  pass

httpd.server_close()
