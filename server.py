# server.py by markrzv
import socket, pickle

class Server:
    def __init__(self, address: str, port: int) -> None:
        self.address = "127.0.0.1"
        self.port = 12312

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.address, self.port))

        print("Server running on", self.address, ":", self.port)
    def listen_for_connections(self):
        # server is waiting for incoming connections (only 1)
        self.server.listen(1)
        connection, address = self.server.accept()

        print("Connection by", address)
    
    def run(self, connection, address):
        
        # recv a string
        data = connection.recv(4096).decode()
        # send a string
        connection.send(bytes("ping", "utf-8"))

        print(data)

        """
        # recv a variable
        data = connection.recv(4096)
        decoded_data = pickle.loads(data)
        # send a variable
        sending_data = pickle.dumps("variable")
        connection.send(sending_data)
        """
        
            

server = Server("127.0.0.1", 12312)  
server.listen_for_connections()     

while True:
    server.run()
