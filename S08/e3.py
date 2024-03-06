import socket

# SERVER IP, PORT
PORT = 1234
IP = "212.128.255.91" # depends on the computer the server is running
flag = True
while flag:
    # -- Ask the user for the message
    message = input("Enter a message to send:")
    # -- Create the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # -- Establish the connection to the Server
    s.connect((IP, PORT))
    # -- Send the user message
    s.send(str.encode(message))
    # -- Close the socket
    s.close()
    flag = False
