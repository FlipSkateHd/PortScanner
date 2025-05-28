import socket

socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria um socket TCP
socketUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Cria um socket UDP

dominio = input("Digite o dominio: ")
portas = input("Digite as portas separadas por virgula (ex: 80, 443): ")
portas = portas.split(",")

portas = [int(porta) for porta in portas]


for porta in portas:
    if socketTCP.connect_ex((dominio, porta)) == 0:  # connect_ex() retorna 0 se o socket conectou
        print(f"Conectado ao servidor na porta {porta}")
    else:
        print(f"Nao foi possivel conectar ao servidor na porta {porta}")

socketTCP.close()