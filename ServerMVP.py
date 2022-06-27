import socket, json


host = '192.168.1.54'
port = 9090
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host , port))
server.listen(5)

def compare(msg):
    message = json.loads(msg)
    key = list(message.keys())
    f1_checksum = key[0]
    f2_checksum = message[f1_checksum]
    if f1_checksum == f2_checksum:
        return 'True'
    else:
        return 'False'
while True:
    communication_socket, address = server.accept()
    print(f'connected to {address}')
    message = communication_socket.recv(1024).decode('utf-8')
    print(f'message from the client is {message} , comparing now...')
    communication_socket.send(compare(message).encode('utf-8'))
    communication_socket.close()
    print(f"connection with {address} ended") 