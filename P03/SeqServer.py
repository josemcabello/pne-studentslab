import socket


def send_response(msg):
    response = ""
    if msg == "PING":
        response = "OK!" + "\n"
        print("PING command!")
        print("OK!")
    elif msg.startswith("GET") and (0 <= int(msg[-1]) < 5):
        response = get_response(msg[-1])
        print("GET")
        print(response)
    elif not(0 <= int(msg[-1]) < 5):
        response = "No sequence like this"
    return response

def get_response(number):
    list_of_sequence = ["ACAGACGACGACACGACTCGACAGATGCGTCG", "GTGTGTGTGTGTGTGTTGGTGTAC", "ACGTACGTACGTACGTACGT", "TGCATGCATGCATGCATGCA", "TTTTTTTTTTTTTTTTTTTTT"]
    number = int(number)
    response = list_of_sequence[number] + "\n"
    return response

def info_response(msg):

    seq = msg[5:]
    print(len(seq))
    print


class SeqServer:

    def __init__(self):
        self.MAX_OPEN_REQUESTS = 5
        self.IP = "127.0.0.1"
        self.PORT = 4321
        print("SEQ Server configured!")

        # create an INET, STREAMing socket
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            serversocket.bind((self.IP, self.PORT))
            serversocket.listen(self.MAX_OPEN_REQUESTS)

            while True:
                # accept connections from outside
                print("Waiting for clients")
                (clientsocket, address) = serversocket.accept()
                msg = clientsocket.recv(2048).decode("utf-8")
                response = send_response(msg)
                send_bytes = str.encode(response)
                # We must write bytes, not a string
                clientsocket.send(send_bytes)
                clientsocket.close()

        except socket.error:
            print("Problems using ip {} port {}. Is the IP correct? Do you have port permission?".format(self.IP, self.PORT))

        except KeyboardInterrupt:
            print("Server stopped by the user")
            serversocket.close()

server = SeqServer()