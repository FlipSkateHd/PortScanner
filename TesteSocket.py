import socket

socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria um socket TCP
socketUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Cria um socket UDP

dominio = input("Digite o dominio: ")
porta = int(input("Digite a porta: "))

if socketTCP.connect_ex((dominio, porta)) == 0:  # connect_ex() retorna 0 se o socket conectou
    print("Conectado ao servidor")
else:
    print("Nao foi possivel conectar ao servidor")


socketTCP.close()