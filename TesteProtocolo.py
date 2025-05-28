## ESTE É UM TESTE DE PROTOCOLO NA REDE LOCAL USANDO O MODULO PSUTIL ##

import psutil

todasConexões = psutil.net_connections(kind='inet')


primeira_conexao = todasConexões[0]
primeiroIp = primeira_conexao.raddr.ip
protocoloPrimeiroIp = primeira_conexao.type

if protocoloPrimeiroIp == 1:
    protocoloPrimeiroIp = "TCP"
else:
    protocoloPrimeiroIp = "UDP"

print(f"Primeiro IP das conexões: {primeiroIp}")
print(f"Protocolo do primeiro IP: { protocoloPrimeiroIp}")