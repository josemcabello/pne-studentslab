from Client0 import *

PRACTICE = 2
EXERCISE = 2

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "192.168.1.45" # your IP address
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)
#...
print(c)
#...
