import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import jinja2 as j

PORT = 8080
socketserver.TCPServer.allow_reuse_address = True
list_of_sequences = ["ACACACACACCACACAAC", "GTGTGGTGTGTGGTGTGTGTGT", "ACGTACGTACGTACGTACGTACGT", "AGAGAGAGAGAGAGGAGAGA", "CTCTCTCTCTCCTCTCTCTCTCTCCT"]
def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents

class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')

        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)
        print(path)

        if path == "/":
            contents = Path("html/index.html").read_text()
        elif path.startswith("/echo"):
            contents = Path("html/ping.html").read_text()
        elif path.startswith("/1echo"):
            text1 = arguments["operation"]
            text = list_of_sequences[int(text1[0])]
            sequence = text1[0]
            print(text1[0])
            contents = read_html_file("get.html").render(context={"body": text, "title": sequence})
        elif path.startswith("/2echo"):
            name = arguments["operation"]
            name1 = name[0]
            if name1 == "RNU6_269P":
                name2 = "Genes/" + name1
            else:
                name2 = "Genes/" + name1 + ".txt"
            text = Path(name2).read_text()
            contents = read_html_file("gene.html").render(context={"body": text, "title": name1})
        elif path.startswith("/myserver"):
            try:
                arguments["chk"] == "on"
                text = str(arguments["msg"]).upper()
            except KeyError:
                text = str(arguments["msg"])
            print(arguments)
            contents = read_html_file("form-e2.html").render(context={"todisplay": text})  # provide a dictionary to build the form
        else:
            contents = Path('html/error.html').read_text()

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()