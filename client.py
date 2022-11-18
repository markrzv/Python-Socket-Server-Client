# client.py by markrzv
import socket, pickle

class Client:
    def __init__(self, server_address: str, server_port: int) -> None:
        self.server_address = server_address
        self.server_port = server_port

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect((self.server_address, self.server_port))

        print("Connected to", self.address, ":", self.port)
    
    def run(self):
        
        # send a string
        self.server.send(bytes("ping", "utf-8"))

        # recv a string
        data = self.server.recv(4096).decode()
        

        print(data)

        """
        # send a variable
        sending_data = pickle.dumps("variable")
        self.server.send(sending_data)
        # recv a variable
        data = self.server.recv(4096)
        decoded_data = pickle.loads(data)
        
        """
        
            

client = Client("127.0.0.1", 12312)  

while True:
    client.run()
