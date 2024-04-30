import http.client
import json
import termcolor

SERVER = "rest.ensembl.org"
ENDPOINTS = "/info/ping"
PARAMS = "?content-type=application/json"
URL = SERVER + ENDPOINTS + PARAMS
print()

print("Dictionary of Genes!")
print("There are 10 genes in the dictionary")
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
print()
genes_values = genes.items()
for e, i in genes_values:
    termcolor.cprint(e, "green", end="")   # el end sirve para q dos lineas esten en la misma
    print(":---->" + i)