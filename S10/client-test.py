from Client0 import *

PRACTICE = 2
EXERCISE = 3

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "212.128.255.67" # your IP address
PORT = 1234

# -- Create a client object
c = Client(IP, PORT)
#...
print(c)
list1 = ["Message 0", "Message 1", "Message 2", "Message 3", "Message 4"]
for e in list1:
    response = c.talk(e)
    print("To server:", e)
    print("From server:", response)