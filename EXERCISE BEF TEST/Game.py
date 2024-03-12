import socket
import random
def send_response(msg, number):
    response = ""
    if int(msg) < int(number):
        response = "It is higher"
    elif int(msg) > int(number):
        response = "It is lower"
    elif int(msg) == int(number):
        response = "You get it"
    return response
class NumberGuesser:
    def __init__(self):
        self.IP = "212.128.255.91"
        self.PORT = 8081
        print("SEQ Server configured!")

        # create an INET, STREAMing socket
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            serversocket.bind((self.IP, self.PORT))
            serversocket.listen()
            self.secret_number = random.randint(1, 100)
            while True:
                # accept connections from outside
                print("Waiting for clients")
                (clientsocket, address) = serversocket.accept()
                msg = clientsocket.recv(2048).decode("utf-8")
                print("Number: " + msg)
                response = send_response(msg, self.secret_number) + "\n"
                self.attempts = 1
                self.list1 = []
                if not(response == "You get it"):
                    self.attempts += 1
                    self.list1.append(msg)
                send_bytes = str.encode(response)
                # We must write bytes, not a string
                clientsocket.send(send_bytes)
                clientsocket.close()

        except socket.error as e:
            print(e)
            print("Problems using ip {} port {}. Is the IP correct? Do you have port permission?".format(self.IP,
                                                                                                         self.PORT))

        except KeyboardInterrupt:
            print("Server stopped by the user")
            serversocket.close()
    def __str__(self):
        return self.attempts, self.list1


server = NumberGuesser()
