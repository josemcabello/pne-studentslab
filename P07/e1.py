import http.client
import json


SERVER = "rest.ensembl.org"
ENDPOINTS = "/info/ping"
PARAMS = "?content-type=application/json"
URL = SERVER + ENDPOINTS + PARAMS
print()
print(f"Server: {SERVER}")
print(f"URL: {URL}")

conn = http.client.HTTPConnection(SERVER)   # aqui hay que poner la primera parte de la url, es decir, el servidor
try:
    conn.request("GET", ENDPOINTS + PARAMS)      # aqui la otra parte de la url, es decir, lo que necesitas de ese servidor
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()


r1 = conn.getresponse() #para conectarse

print(f"Response received!: {r1.status} {r1.reason}\n")

data1 = r1.read().decode("utf-8") #para conseguir la informacio pero en str
person = json.loads(data1)         #para conseguir la informacion en formato json

if person["ping"] == 1:
    print("Ping OK!  The database is running!")