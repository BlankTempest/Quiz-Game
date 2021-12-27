'''import socket
from _thread import *
#import sys

#default parameters, ipv4 and tcp prot
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#if we pass an empty string, it will listen to incoming connections 
#from other computers are well
#passing 127.0.0.1 will isten only to the calls made within local comp
server = 'localhost'
#port should be open
port = 5555

#gethostbyname finds the ip
server_ip = socket.gethostbyname(server)


#connects to the server
try:
    #idk if server and server_ip makes a difference
    # but i'll use server_ip just to be sure
    s.bind((server_ip,port))

except socket.error as e:
    print(str(e))


#no of connections
s.listen(2)
print("Waiting for a connection")

#id of player 1
currentId = "0"

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

#mouse pos of both players
pos = ["0:50,50", "1:100,100"]


def threaded_client(conn):
    global currentId, pos

    #send pos to the client
    conn.send(str.encode(currentId))
    #id of player 1 is now updated to player 2
    currentId = "1"
    reply = ''
    while True:
        #keeps trying until an error occurs
        # then performs the except part
        try:

            #recieve data, 2048 bits, less bits = faster transfer
            data = conn.recv(2048)
            #decode the encoded str that we sent
            reply = data.decode('utf-8')

            if not data:
                #not getting data,
                conn.send(str.encode("Goodbye"))
                #or just print("Disconnected")
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

            #we encode b4 sending data to the server
            conn.sendall(str.encode(reply))
        except:
            break

    #close connection
    print("Connection Closed")
    conn.close()

while True:
    #establish connection, accepts any conn
    conn, addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn,))'''