import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import jinja2 as j
import http.client
import json

PORT = 8080
socketserver.TCPServer.allow_reuse_address = True
def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents
def con_ensembl(ENDPOINTS):
    SERVER = "rest.ensembl.org"
    PARAMS = "?content-type=application/json"

    conn = http.client.HTTPConnection(SERVER)   # aqui hay que poner la primera parte de la url, es decir, el servidor
    try:
        conn.request("GET", ENDPOINTS + PARAMS)      # aqui la otra parte de la url, es decir, lo que necesitas de ese servidor
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()
    r1 = conn.getresponse()
    data1 = r1.read().decode("utf-8")
    person = json.loads(data1)
    return person



class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')

        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)
        print(path)
        try:
            if path == "/":
                contents = Path("html/index.html").read_text()

            elif path.startswith("/listSpecies"):
                ENDPOINTS = "/info/species"
                person = con_ensembl(ENDPOINTS)
                n_o_species = len(person["species"])
                if len(arguments) == 0:
                    n_o_lspecies = 10000000
                    info = person["species"][:int(n_o_lspecies)]
                    n_o_lspecies = "undefined"
                else:
                    n_o_lspecies = arguments["limit"][0]
                    info = person["species"][:int(n_o_lspecies)]
                info_lspecies = []
                for e in info:
                    a = e['display_name']
                    info_lspecies.append(a)

                contents = read_html_file("listSpecies.html").render(context={"n_o_species": n_o_species, "n_o_lspecies": n_o_lspecies, "info_lspecies": info_lspecies})

            elif path.startswith("/karyotype"):
                text = arguments["species"][0]
                text1 = text.replace(" ", "%20")
                ENDPOINTS = "/info/assembly" + "/" + text1
                person = con_ensembl(ENDPOINTS)
                info_lspecies = person['karyotype']
                contents = read_html_file("karyotype.html").render(context={"info_lspecies": info_lspecies})

            elif path.startswith("/chromosomeLength"):
                text1 = arguments["species"][0]
                number_of_chro = arguments["chromo"][0]
                ENDPOINTS = "/info/assembly" + "/" + text1
                person = con_ensembl(ENDPOINTS)
                info_lspecies = person['karyotype']
                i = 0
                for e in info_lspecies:
                    if e == number_of_chro:
                        break
                    elif i == len(info_lspecies) - 1:
                        i = "whatever"
                    else:
                        i += 1
                l_o_chr = person["top_level_region"][i]['length']
                contents = read_html_file("chromosomeLength.html").render(context={"l_o_chr": l_o_chr})
            elif path.startswith("/geneSeq"):
                gene = arguments["gene"][0]
                ENDPOINTS = "/info/genomes/human"
                person = con_ensembl(ENDPOINTS)
                print(gene)
                contents = read_html_file("chromosomeLength.html").render(context={"gene": gene, "sequence": sequence})

            elif path.startswith("/geneInfo"):
                gene = arguments["gene"][0]
                ENDPOINTS = "/info/genomes/human"
                person = con_ensembl(ENDPOINTS)
                contents = read_html_file("chromosomeLength.html").render(context={"gene": gene, "start": start, "end": end, "n_chromo": n_chromo})

            elif path.startswith("/geneCalc"):
                gene = arguments["gene"][0]
                ENDPOINTS = "/info/genomes/human"
                person = con_ensembl(ENDPOINTS)
                contents = read_html_file("chromosomeLength.html").render(context={"gene": gene, "length": length, "percentage": percentage})

            elif path.startswith("/geneList"):
                chromo = arguments["chromo"][0]
                start = arguments["start"][0]
                end = arguments["end"][0]
                ENDPOINTS = "/info/assembly/homo_sapiens/" + chromo
                person = con_ensembl(ENDPOINTS)
                print(person)
                contents = read_html_file("chromosomeLength.html").render(context={"chromo": chromo, "start": start, "end": end, "l_genes": l_genes})

            else:
                contents = Path('html/error.html').read_text()

        except Exception:
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