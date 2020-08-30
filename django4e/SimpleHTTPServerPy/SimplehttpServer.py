from socket import socket, AF_INET, SOCK_STREAM, SHUT_WR


def createserver():
    # this function creates the necessary server
    # this server waits for upcoming requests and make the response

    servsocket = socket(AF_INET, SOCK_STREAM)
    # 👆🏻 socket to listen to incoming requests

    try:
        servsocket.bind(("localhost", 8081))

        servsocket.listen(5)
        # 👆🏻 this function will not let other requests to be denied
        # it will ask the OS to hold other requests temporarly and
        # accept it after the first one finishes

        while(1):
            # 👇🏻 will accept the request
            (clientsocket, _) = servsocket.accept()

            rd = clientsocket.recv(5000).decode()
            # 👆🏻 this will take the request data and decode it to Unicode
            # 👇🏻 we split the data in the request
            pieces = rd.split("\n")

            if len(pieces) > 1:
                print(pieces[0])

            # 👇🏻 following are the data returned to the client
            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello World!!</body></html>\r\n\r\n"

            # 👇🏻 sends all the data to the client while encoding it to utf-8 for the socket
            clientsocket.sendall(data.encode())
            clientsocket.shutdown(SHUT_WR)
            # 👆🏻 we close the socket
            # this loop will continue the process of
            # handling request ↔ returning response
            # until something happens

    # 👇🏻 exception if we want to close the server or anything bad happens to the server
    except KeyboardInterrupt:
        print("Ok Bye!! Shutting Down...\n")
    except Exception as exc:
        print("Error:\n")
        print(exc)

    servsocket.close()


print("Server is listening at http://localhost:8081")
# 👇🏻 runs the server
createserver()
