try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
try:
    urllib2.urlopen("http://www.google.com",timeout=2)
    print("[+] İnternet bağlantısı başarılı")
except urllib2.URLERROR:
    print("[-] İnternet bağlantısı hatası")
