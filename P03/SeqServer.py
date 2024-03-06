import socket

class SeqServer:

    def __int__(self):
        self.MAX_OPEN_REQUESTS = 5
        self.IP = "127.0.0.1"
        self.PORT = 1234
        print("SEQ Server configured!")

        ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # -- Step 2: Bind the socket to server's IP and PORT
        ls.bind((self.IP, self.PORT))

        # -- Step 3: Configure the socket for listening
        ls.listen()
        number_con = 0

        # create an INET, STREAMing socket
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.serversocket.bind((self.IP, self.PORT))
            self.serversocket.listen(self.MAX_OPEN_REQUESTS)

            while True:
                # accept connections from outside
                print("Waiting for clients")
                (clientsocket, address) = self.serversocket.accept()
                self.clientsocket = clientsocket

                # Another connection!e
                number_con += 1

                # Print the connection number
                print("CONNECTION: {}. From the IP: {}".format(number_con, address))

                # Read the message from the client, if any
                msg = clientsocket.recv(2048).decode("utf-8")

                if msg == "PING":
                    response = "OK"
                send_bytes = str.encode(response)
                # We must write bytes, not a string
                self.clientsocket.send(send_bytes)
                self.clientsocket.close()

        except socket.error:
            print("Problems using ip {} port {}. Is the IP correct? Do you have port permission?".format(IP, PORT))

        except KeyboardInterrupt:
            print("Server stopped by the user")
            serversocket.close()
    def PING(self):
        if self.msg == "PING":
            send_bytes = str.encode("OK")
            # We must write bytes, not a string
            self.clientsocket.send(send_bytes)
            self.clientsocket.close()

