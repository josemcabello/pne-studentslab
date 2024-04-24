import http.client
import json
import termcolor
from Seq1 import *



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
while True:
    gene = input("Write the gene name:")
    try:
        ID = genes[gene]

    except KeyError:
        print("Key not found")

SERVER = "rest.ensembl.org"
ENDPOINTS = "/sequence/id"
PARAMS = "?content-type=application/json"
ID = genes[gene]
URL = SERVER + ENDPOINTS + "/" + ID + PARAMS


print()
print(f"Server: {SERVER}")
print(f"URL: {URL}")


conn = http.client.HTTPConnection(SERVER)   # aqui hay que poner la primera parte de la url, es decir, el servidor
try:
    conn.request("GET", ENDPOINTS + "/" + ID + PARAMS)      # aqui la otra parte de la url, es decir, lo que necesitas de ese servidor
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()


r1 = conn.getresponse() #para conectarse

print(f"Response received!: {r1.status} {r1.reason}\n")

data1 = r1.read().decode("utf-8")
person = json.loads(data1)
print(person)
print()
termcolor.cprint("Gene:  ", "green", end="")
print(gene)
termcolor.cprint("Description:  ", "green", end="")
print(person["desc"])

