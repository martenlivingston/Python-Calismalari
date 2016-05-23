import hashlib

md5hash=raw_input("Kırılıcak Hashi Giriniz:)
wrdLst=raw_input("Wordlistiniz konumunu giriniz:")
wordlist=open(wrdLst,"r").readLines()

for key in wordlist:
    key=key.strip()
    kirilan=hashlib.md5(key).hexdigest() #wordlistden aldığımız kelimeyi md5 ile şifreledik
    if kirilan == md5hash:
        print("Md5 ile şifrelenen veriniz " + key)
        break
