import time
import socket
server_port = 5000
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
start = time.time()
input_s = "Buna, server!"
client_socket.sendto(bytes(input_s, encoding='utf8'), ('127.0.0.1', server_port))
print('Timpul cand sa trimis mesajul: ', (time.time()-start)*1000, ' ms')
input_s_modified, address = client_socket.recvfrom(65535)
print ('[CLIENT] Raspunsul de la server {}, este: "{}"'.format(address, str(input_s_modified.decode('utf8'))))
print ("Timpul cand a ajuns mesajul: ", (time.time()-start)*1000, ' ms')
client_socket.close()
time.sleep(1)
