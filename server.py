import socket
from _thread import *
import sys

#default parameters, ipv4 and tcp prot
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#if we pass an empty string, it will listen to incoming connections 
#from other computers are well
#passing 127.0.0.1 will isten only to the calls made within local comp
server = 'localhost'
port = 5555

#get host by name finds the ip
server_ip = socket.gethostbyname(server)

#connects to the server
try:
    s.bind((server,port))

except socket.error as e:
    print(str(e))

#no of connections
s.listen(2)
print("Waiting for a connection")

#id of player
currentId = "0"

#mouse pos
pos = ["0,0", "0,0"]


def threaded_client(conn):
    global currentId, pos

    #send pos to the client
    conn.send(str.encode(currentId))
    #to player 2
    currentId = "1"
    reply = ''
    while True:
        #keeps trying until an error occurs
        # then performs the except part
        try:

            #recieve data
            data = conn.recv(2048)
            #parse it 
            reply = data.decode('utf-8')

            if not data:
                conn.send(str.encode("Goodbye"))
                break
            else:
                print("Recieved: " + reply)
                arr = reply.split(":")
                id = int(arr[0])
                pos[id] = reply

                if id == 0: nid = 1
                if id == 1: nid = 0

                reply = pos[nid][:]
                print("Sending: " + reply)

            conn.sendall(str.encode(reply))
        except:
            break

    #close connection
    print("Connection Closed")
    conn.close()

while True:
    #establish connection
    conn, addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn,))