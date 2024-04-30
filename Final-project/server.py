import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import jinja2 as j

PORT = 8080
socketserver.TCPServer.allow_reuse_address = True
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

        elif path.startswith("/listSpecies"):
            contents = read_html_file("listSpecies.html")

        elif path.startswith("/karyotype"):

            text1 = arguments["specie"]
            text = text1[0]
            sequence = text1[0]
            print(text)
            contents = read_html_file("karyotype.html").render(context={"body": text, "title": sequence})

        elif path.startswith("/chromosomeLength"):
            name = arguments["specie"]
            name1 = name[0]
            if name1 == "RNU6_269P":
                name2 = "Genes/" + name1
            else:
                name2 = "Genes/" + name1 + ".txt"
            text = Path(name2).read_text()
            contents = read_html_file("chromosomeLength.html").render(context={"body": text, "title": name1})

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