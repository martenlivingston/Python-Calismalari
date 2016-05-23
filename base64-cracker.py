import base64

sifre=raw_input("Şifrelenmiş veriyi giriniz: ")

print("Şifre Çözülüyor...")

#sifre cozme islemi burada basliyor
sifre2=base64.b64decode(encoded)

print("Sifre bulundu : " + sifre2 )
