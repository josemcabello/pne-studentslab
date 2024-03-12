from Game import *
from Client0 import *
IP = "212.128.255.91"
PORT = 8081

# -- Create a client object
c = Client(IP, PORT)

while True:
    number = input("Enter a number:")
    print(number)
    response = c.talk(number)
    print(response)
    if response == "You get it":
        break

