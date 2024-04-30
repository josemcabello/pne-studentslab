import socket

# Configure the Server's IP and PORT
PORT = 8080
IP = "212.128.255.85" # this IP address is local, so only requests from the same machine are possible

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")
N = 1
while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")

    try:
        (cs, address) = ls.accept()
    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")

        # -- Close the listenning socket
        ls.close()

        # -- Exit!
        exit()

    # -- Execute this part if there are no errors
    else:

        print("CONNECTION",  N, ". Client IP, PORT:", address)

        # -- Read the message from the client
        # -- The received message is in raw bytes
        msg_raw = cs.recv(2048)

        # -- We decode it for converting it
        # -- into a human-redeable string
        msg = msg_raw.decode()

        # -- Print the received message
        print(f"Message received: {msg}")

        # -- Send a response message to the client
        response = "ECHO: " + str(msg + "\n")

        # -- The message has to be encoded into bytes
        cs.send(response.encode())
        N += 1
        # -- Close the data socket
        cs.close()