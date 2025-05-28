import socket

socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Cria um socket TCP
socketUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Cria um socket UDP

dominio = "www.google.com"
porta = 80

if socketTCP.connect_ex((dominio, porta)) == 0:
    print("Conectado ao servidor")
else:
    print("Nao foi possivel conectar ao servidor")


socketTCP.close()