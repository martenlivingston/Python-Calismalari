import os
dizin="."
dizinBoyut=0

fsizedicr={'Bytes': 1, 'Kibobytes': float(1)/1024,'Megabytes': float(1)/(1024*1024),'Gigabytes': float(1)/(1024*1024*1024)}

for (path,dirs,files)in os.walk(dizin):
    for dosya in files:
        dadi=os.path.join(path,dosya)
        dizinBoyut+=os.path.getsize(dadi)
for key in fsizedicr:
    print("Folder size: ". str(round(fsizedicr[key]*dizinBoyut,2)). key)
