import socket
from Seq1 import *

def send_response(msg):
    response = ""
    if msg == "PING":
        print("PING command!")
        response = "OK!" + "\n"
        print("OK!")
    elif msg.startswith("GET") and (0 <= int(msg[-1]) < 5):
        response = get_response(msg[-1])
        print("GET")
        print(response)
    elif msg.startswith("INFO"):
        print("INFO")
        response = info_response(msg)
    elif msg.startswith("COMP"):
        print("COMP")
        response = comp_response(msg)
        print(response)
    elif msg.startswith("REV"):
        print("REV")
        response = rev_response(msg)
        print(response)
    return response

def get_response(number):
    list_of_sequence = ["ACAGACGACGACACGACTCGACAGATGCGTCG", "GTGTGTGTGTGTGTGTTGGTGTAC", "ACGTACGTACGTACGTACGT", "TGCATGCATGCATGCATGCA", "TTTTTTTTTTTTTTTTTTTTT"]
    number = int(number)
    response = list_of_sequence[number] + "\n"
    return response

def info_response(msg):
    letters = ["A", "C", "G", "T"]
    seq = msg[5:]
    count1 = [seq.count("A"), seq.count("C"), seq.count("G"), seq.count("T")]
    porc = [str(100 * seq.count("A") / len(seq)) + " %", str(100 * seq.count("C") / len(seq)) + " %", str(100 * seq.count("G") / len(seq)) + " %", str(100 * seq.count("T") / len(seq)) + " %"]
    print(len(seq))
    i = 0
    response = ""
    while i < 4:
        a = str(letters[i]) + " : " + str(count1[i]) + " (" + str(porc[i]) + ")" + "\n"
        print(a)
        response += a
        i += 1
    return response

def rev_response(msg):
    seq = msg[4:]
    rev = Seq(seq)
    new_seq = rev.reverse()
    return new_seq
def comp_response(msg):
    seq = msg[5:]
    comp_seq = Seq(seq)
    new_seq = comp_seq.complement()
    return new_seq
class SeqServer:

    def __init__(self):
        self.MAX_OPEN_REQUESTS = 5
        self.IP = "127.0.0.1"
        self.PORT = 3333
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
                response = send_response(msg) + "\n"
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