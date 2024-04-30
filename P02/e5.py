from Client0 import *

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "212.128.255.85" # your IP address
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)
#...
print(c)
list1 = []
s = Seq()
s1 = s.read_fasta("FRAT1.txt")
num = 0
seq = ""
for e in s1:
    seq += e
    if len(seq) == 10:
        list1.append(seq)
        seq = ""
        num += 1
    if num == 5:
        break
w0 = "Sending " + str("FRAT1") + " Gene to the server, in fragments of 10 bases ..."
w = "Gene FRAT1: " + s1
response0 = c.talk(w0)
response01 = c.talk(w)
print(w)
num1 = 1
for i in list1:
    ww = "Fragment " + str(num1) + " : " + str(i)
    response1 = c.talk(ww)
    print(ww)
    num1 += 1
