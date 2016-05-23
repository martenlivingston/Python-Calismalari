import time
import webbrowser

totalBreaks=5
countBreaks=0

print("geçerli zaman dilimi \n"+ time.ctime())
while(countBreaks<totalBreaks):
    time.sleep(0.5)
    webbrowser.open("www.google.com")
    countBreaks=countBreaks+1
