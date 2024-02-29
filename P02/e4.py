from Client0 import *

PRACTICE = 2
EXERCISE = 1

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "212.128.255.91" # your IP address
PORT = 1234

# -- Create a client object
c = Client(IP, PORT)
#...
print(c)
for e in seq_list:
    s = Seq()
    s1 = s.read_fasta("U5.txt")
    a = "Sending U5 Gene to the server..."
    print(a)
    response1 = c.talk(a)
    response = c.talk(s1)
    print("From server:", "\n", "\n" + str(response))
    print("To server:", s1)
    print("From server:", "\n", "\n" + str(response))