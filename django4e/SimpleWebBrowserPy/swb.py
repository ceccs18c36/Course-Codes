import socket

# sockets are built into python.
# this lib is used to connect to the server,send data and to recieve data from the server

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.socket is used to make something to make the connections
# just like a phone in a telephone communication

mysocket.connect(("data.pr4e.org", 80))
# the above line indicate that we are making the call to the server
# i.e, connecting to the server
# to the specific domain and port given as argument

req_cmd = "GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n".encode()
# req_cmd is the place we are sending the request to recieve our file
# \r\n\r\n is used to indicate a (return & newline)x2
# we encode the req to UTF-8 since Unicode is not used by the internet
# (the req_cmd is in Unicode which is used in everything nowadays)

mysocket.send(req_cmd)
# since we are the client we need to send the req first
# so we send our req to the server using mysocket.send()

while True:
    # after sending the packets we begin to recieve data(piece by piece)

    data = mysocket.recv(512)
    # we recieve 512 charcters each time

    if len(data) < 1:
        # this continues till we stop recieving data
        break

    print(data.decode(), end="")
    # we use decode() here to decode the data into Unicode
    # since the data recieved from the server is in UTF-8
    # we need to decode it since print() uses Unicode

mysocket.close()
# closing the connection after data is recieved

# -----------------👇🏻----------------
# data recieved from the server is in data.txt
