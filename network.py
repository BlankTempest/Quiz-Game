'''import socket


class Network:

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_ip = socket.gethostbyname('localhost')
        self.host = server_ip # For this to work on your machine this must be equal to the ipv4 address of the machine running the server
                                    # You can find this address by typing ipconfig in CMD and copying the ipv4 address. Again this must be the servers
                                    # ipv4 address. This feild will be the same for all your clients.
        self.port = 5555
        self.addr = (self.host, self.port)
        #calls connect
        self.id = self.connect()

    def connect(self):
        #we send data
        self.client.connect(self.addr)
        #then recive data and then decode it
        return self.client.recv(2048).decode()

    def send(self, data):
        """
        :param data: str
        :return: str
        """
        try:
            #we send encoded data
            self.client.send(str.encode(data))
            #then recieve decoded data
            reply = self.client.recv(2048).decode()
            return reply
        except socket.error as e:
            return str(e)'''