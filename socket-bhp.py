import socket

hedef_host="www.google.com"
hedef_port=80

#socket objemizi olusturalim
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#client a baglanalim

client.connect((hedef_host,hedef_port))

#veri gonderelim

client.send("Merhaba")

#veri alalim

response=client.recv(4069)

print(response)
