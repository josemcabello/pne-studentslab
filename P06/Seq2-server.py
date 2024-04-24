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

def info_response(msg):
    letters = ["A", "C", "G", "T"]
    seq = msg[5:]
    count1 = [seq.count("A"), seq.count("C"), seq.count("G"), seq.count("T")]
    porc = [str(100 * seq.count("A") / len(seq)) + " %", str(100 * seq.count("C") / len(seq)) + " %", str(100 * seq.count("G") / len(seq)) + " %", str(100 * seq.count("T") / len(seq)) + " %"]
    print(len(seq))
    i = 0
    response = "Sequence: " + seq + "\n" + "Total length:" + str(len(seq)) + "\n"
    while i < 4:
        a = str(letters[i]) + " : " + str(count1[i]) + " (" + str(porc[i]) + ")" + "\n"
        print(a)
        response += a
        i += 1
    return response

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
            secuence = arguments["msg"][0]

            if arguments["operation"] == "Info":
                t_op = "Info"
                result = info_response((secuence))
                contents = read_html_file("operation.html").render(context={"secuence": secuence, "operation": t_op, "result": result})
            elif arguments["operation"] == "Comp":
                t_op = "Comp"
                contents = read_html_file("operation.html").render(context={"secuence": secuence, "operation": t_op, "result": result})
            elif arguments["operation"] == "Rev":
                t_op = "Rev"
                contents = read_html_file("operation.html").render(context={"secuence": secuence, "operation": t_op, "result": result})


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