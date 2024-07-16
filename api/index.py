from http.server import BaseHTTPRequestHandler
import cgi
import ast
from cron.cron_executer import cron_execute
 
class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('Hello'.encode('utf-8'))
        return
    
    def do_POST(self):
        
        form = cgi.FieldStorage(
            fp=self.rfile, 
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'],
                     })
        try:
            if "data" in form:
                # Assuming "data" contains multiple items
                data = ast.literal_eval(form.getvalue('data'))
                final_message = cron_execute(data)
                self.send_response(200)
                self.send_header('Content-type','text/plain')
                self.end_headers()
                self.wfile.write(final_message.encode('utf-8'))
            else:
                self.send_response(400)
                self.send_header('Content-type','text/plain')
                self.end_headers()
                self.wfile.write(b"No data field found.")
        except Exception as e:
            self.send_response(400)
            self.send_header('Content-type','text/plain')
            self.end_headers()
            self.wfile.write(b"Invalid Data.")
        return 