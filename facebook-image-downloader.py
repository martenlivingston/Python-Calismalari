import urllib
from urllib import urlretrieve
import re
kaydet = '~/fbimage'
uzanti ='.jpg'
for i in range (3,1000000):
    x=urllib.urlopen("http://facebook.com/%s"%i)
    html="".join(x)
    match = re.search(r'<img class="profilePic img" src="\S+',html)
if match:
    xc=match.group()[33:-1]
    urlretrieve(xc,kaydet+'_'+str(i)+uzanti)
