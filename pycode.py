from http.server import HTTPServer, BaseHTTPRequestHandler
import cgi
with open('index.html', 'r') as f:
    html_string = f.read()

class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith('/'):
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()
            a_string = ''
            a_string += html_string
            self.wfile.write(a_string.encode())

def main():
    PORT = 8000
    server_address = ('localhost', PORT)
    server = HTTPServer(server_address, requestHandler)
    print("server is running on port %s" % PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()
