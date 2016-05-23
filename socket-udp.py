import socket

hedef_host="127.0.0.1"
hedef_port=80

client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.sendto("AAABBBCCC",(hedef_host,hedef_port))

data,addr=client.recvfrom(4096)

print(data)
