import http.client
import json
import termcolor

SERVER = "rest.ensembl.org"
ENDPOINTS = "/sequence/id"
PARAMS = "?content-type=application/json"
URL = SERVER + ENDPOINTS + "/ENSG00000207552" + PARAMS
print()
print(f"Server: {SERVER}")
print(f"URL: {URL}")
genes = {"ADA": "ENSG00000196839",
         "FRAT1": "ENSG00000165879",
         "FXN": "ENSG00000165060",
         "RNU6_269P": "ENSG00000212379",
         "MIR633": "ENSG00000207552",
         "TTTY4C": "ENSG00000228296",
         "RBMY2YP": "ENSG00000227633",
         "FGFR3": "ENSG00000068078",
         "KDR": "ENSG00000128052",
         "ANK2": "ENSG00000145362"
          }
conn = http.client.HTTPConnection(SERVER)   # aqui hay que poner la primera parte de la url, es decir, el servidor
try:
    conn.request("GET", ENDPOINTS + "/ENSG00000207552" + PARAMS)      # aqui la otra parte de la url, es decir, lo que necesitas de ese servidor
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()


r1 = conn.getresponse() #para conectarse

print(f"Response received!: {r1.status} {r1.reason}\n")

data1 = r1.read().decode("utf-8")
person = json.loads(data1)
print()
termcolor.cprint("Gene:  ", "green", end="")
print("MIR633")
termcolor.cprint("Description:  ", "green", end="")
print(person["desc"])
termcolor.cprint("Bases:  ", "green", end="")
print(person["seq"])
