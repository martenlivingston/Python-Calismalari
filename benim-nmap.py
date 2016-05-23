import nmap

hedefHost=input("Hedef hostu giriniz: ")
hedefPort=input("Hedef portu giriniz: ")

portTara=nmap.PortScanner()
portTara.scan(hedefHost,hedefPort)

print(portTara)
