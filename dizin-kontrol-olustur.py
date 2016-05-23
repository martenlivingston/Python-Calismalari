import os
try:
    masa = os.path.expanduser("~/Masaüstü")         
    print (masa)
    if not os.path.exists(masa+'/dizin'):
        os.makedirs(masa+'/dizin')
except Exception as e:
        print (e)
