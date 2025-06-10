import socket

def manualPorts():
    socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria um socket TCP
    socketUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Cria um socket UDP
    domain = input("Insert your domain: ")
    ports = input("Insert your ports with an comma (default: 80, 443): ")
    ports = ports.split(",")

    if ports[0] == "":
        ports = [80, 443]    
    else:
        ports = [int(port) for port in ports]


    for port in ports:
        if socketTCP.connect_ex((domain, port)) == 0:  # connect_ex() retorna 0 se o socket conectou
            print(f"Open port:/ {port}")
        else:
            print(f"Closed port:/ {port}")

        socketTCP.close()



def fullScan():
    LHOST = input("Insert host: ")
    for PORTS in range (1,6535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if s.connect_ex((LHOST, PORTS)) == 0:
            print(f"Open port:/ {PORTS}")
        else:
            pass
    

def main():
    mode = input("Insert 1 for manual ports or 2 for full scan: ")
    if mode == "1":
        manualPorts()
    else:
        fullScan()

main()