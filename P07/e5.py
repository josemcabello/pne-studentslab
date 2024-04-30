import http.client
import json
import termcolor
from Seq1 import *

def most_frequent_base(sequence):
    seq = ""
    a = 0
    c = 0
    g = 0
    t = 0
    for e in sequence:
        if e == "A":
            a += 1
        elif e == "C":
            c += 1
        elif e == "G":
            g += 1
        elif e == "T":
            t += 1
    x = 0
    if x < a:
        x = a
    if x < c:
        x = c
    if x < g:
        x = g
    if x < t:
        x = t

    if x == a:
        solution = "A"
    elif x == c:
        solution = "C"
    elif x == g:
        solution = "G"
    elif x == t:
        solution = "T"
    return solution

genes = {"ADA": "ENSG00000196839",
         "FRAT1": "ENSG00000165879",
         "FXN": "ENSG00000165060",
         "RNU6_269P": "ENSG00000212379",
         "MIR633": "ENSG00000207552",
         "TTTY4C": "ENSG00000228296",
         "RBMY2YP": "ENSG00000227633",
         "FGFR3": "ENSG00000068078",
         "KDR": "ENSG00000128052",
         "ANK2": "ENSG00000145362"}
for gene, ID in genes.items():

    SERVER = "rest.ensembl.org"
    ENDPOINTS = "/sequence/id"
    PARAMS = "?content-type=application/json"
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
    print()
    termcolor.cprint("Gene:  ", "green", end="")
    print(gene)
    termcolor.cprint("Description:  ", "green", end="")
    print(person["desc"])
    seq1 = person["seq"]
    seq = Seq(seq1)
    seq_l = seq.len()
    termcolor.cprint("Total  length:  ", "green", end="")
    print(seq_l)
    seq_info = seq.seq_count(seq1)
    for e, i in seq_info.items():
        print(str(e) + ":" + str(i))
    m_frequent = most_frequent_base(seq1)
    termcolor.cprint("Most frequent Base:  ", "green", end="")
    print(m_frequent)
