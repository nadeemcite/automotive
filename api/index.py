import ast
from email.parser import BytesParser
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs

from cron.cron_executer import cron_execute


class Handler(BaseHTTPRequestHandler):
    """
    A simple HTTP request handler supporting GET and POST methods.

    GET:
        A health check endpoint that returns a plain text "Hello" message.

    POST:
        An endpoint to execute automation. It expects a URL-encoded form body
        containing a "data" parameter. The "data" parameter should be a string
        representation of a Python literal. This literal is safely evaluated
        using ast.literal_eval and passed to the cron_execute function.
    """

    def do_GET(self):
        """
        Handle GET requests for health check.

        Responds with HTTP 200 and a plain text message "Hello".
        """
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write("Hello".encode("utf-8"))

    def do_POST(self):
        """
        Handle POST requests to execute automation.

        Expected Request:
            - Content-Type: application/x-www-form-urlencoded
            - Body: A URL-encoded string with a 'data' field.

        Processing:
            - Reads the content length from the headers.
            - Decodes the request body and parses it using urllib.parse.parse_qs.
            - If a 'data' parameter is present, it evaluates the string using
              ast.literal_eval and passes the result to cron_execute.
            - Returns the message produced by cron_execute on success.

        Responses:
            - HTTP 200: When automation executes successfully.
            - HTTP 400: For unsupported content types (like multipart/form-data)
                       or when errors occur (e.g., missing 'data' field or evaluation errors).
        """
        content_length = int(self.headers.get("Content-Length", 0))
        raw_data = self.rfile.read(content_length)
        headers = BytesParser().parsebytes(self.headers.as_bytes())
        content_type = headers.get("Content-Type", "")

        if "multipart/form-data" in content_type:
            self.send_response(400)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"multipart/form-data is not supported.")
            return

        try:
            form_data = raw_data.decode("utf-8")
            params = parse_qs(form_data)

            if "data" in params:
                data_str = params["data"][0]
                data = ast.literal_eval(data_str)
                final_message = cron_execute(data)
                self.send_response(200)
                self.send_header("Content-type", "text/plain")
                self.end_headers()
                self.wfile.write(final_message.encode("utf-8"))
            else:
                self.send_response(400)
                self.send_header("Content-type", "text/plain")
                self.end_headers()
                self.wfile.write(b"No data field found.")
        except Exception as e:
            print(f"Error processing POST request: {e}")
            self.send_response(400)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(str(e).encode("utf-8"))
