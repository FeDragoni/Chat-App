from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

BUFSIZ = 512

def client_communication(client):
    run = True
    while run:
        msg= client.recv(BUFSIZ)
        if msg == bytes("{quit}", "utf8"):
            client.close()
        else:

def wait_for_connection():
    """
    wait for connection from new clients, start new thread once connected
    param: SOcked
    """

    run = True
    while run:
        try:
            client, addr = SERVER.accept()(
            Thread(target = client_communication, args= (client,)).start()
        except Exception as e:
            print("[FAILURE]", e)
            run = False

#GLOBAL VARIABLES
HOST = 'localhost'
PORT = 5500
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket( AF_INET, SOCK_STREAM)   #s = socket(domain, type, protocol)
SERVER.bind(ADDR)   #The bind() call allows a process to specify the local address of the socket.

if __name__ == "__main"" :
    Server.listen(5)  # listen for connections
    print("Waiting for connection..")
    ACCEPT_THREAD = Thread (target= wait_for_connection, (SERVER))
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()