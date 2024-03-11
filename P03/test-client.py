from SeqServer import *
from Client0 import *
IP = "212.128.255.66"
PORT = 1234

# -- Create a client object
c = Client(IP, PORT)
print(c)
print("* Testing PING...")
ping = c.ping()
print("* Testing GET...")
a = 0
while a < 5:
    aa = "GET " + str(a)
    response = c.talk(aa)
    a += 1
    print(aa + ": " + str(response))

print("* Testing INFO...")
b = "INFO ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA"
response1 = c.talk(b)
print(response1)

print("* Testing COMP")
d = "COMP ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA"
print(d)
response2 = c.talk(d)
print(response2)

print("* Testing REV")
e = "REV ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA"
print(e)
response3 = c.talk(e)
print(response3)

list12 = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
print("* Testing GENE...")
for ee in list12:
    print(ee)
    e1 = "GENE " + str(ee)
    response4 = c.talk(e1)
    print(response4)