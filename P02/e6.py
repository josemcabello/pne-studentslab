from Client0 import *

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "212.128.255.85"# your IP address
PORT = 8080
c = Client(IP, PORT)
print(c)
PORT1 = 8081
c1 = Client(IP, PORT1)
print(c1)

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
    if num == 10:
        break
w0 = "Sending " + str("FRAT1") + " Gene to the server, in fragments of 10 bases ..."
response0 = c.talk(w0)
response01 = c1.talk(w0)
w = "Gene FRAT1: " + s1
print(w)
num1 = 1
for i in list1:
    if num1 % 2 == 1:
        ww = "Fragment " + str(num1) + " : " + str(i)
        response1 = c.talk(ww)
        print(ww)
    else:
        ww = "Fragment " + str(num1) + " : " + str(i)
        response1 = c1.talk(ww)
        print(ww)
    num1 += 1