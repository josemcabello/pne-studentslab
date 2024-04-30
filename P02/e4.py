from Client0 import *

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "212.128.255.85" # your IP address
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)
#...
print(c)
list_of_files = ["ADA.txt", "FRAT1.txt", "U5.txt"]
for e in list_of_files:
    s = Seq()
    s1 = s.read_fasta(e)
    ee = e[:-4]
    a = "Sending " + str(ee) + " Gene to the server..."
    print(a)
    response1 = c.talk(a)
    response = c.talk(s1)
    print("From server:", "\n", "\n" + str(response))
    print("To server:", s1)
    print("From server:", "\n", "\n" + str(response))