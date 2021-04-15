import socket
server_port = 5000
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('127.0.0.1', server_port))
print ('[SERVER] Asteapta conectiunea: {}'.format(server_socket.getsockname()))
while True:
    message, address = server_socket.recvfrom(65535)
    print ('[SERVER] Clientul {}, A trimis: {}'.format(address, repr(message)))
    server_socket.sendto(bytes('Serverul \
a trimis inapoi: "{}".'.format(message), encoding='utf8'), address)
server_socket.close()

