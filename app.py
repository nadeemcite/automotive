from http.server import HTTPServer

from api.index import Handler


def run(server_class=HTTPServer, handler_class=Handler, port=8000):
    """
    Starts an HTTP server on the specified port.
    """
    server_address = ("", port)  # Listen on all available interfaces
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run(port=8000)