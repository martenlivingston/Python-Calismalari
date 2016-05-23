import os
try:
    masa = os.path.expanduser("~/Masaüstü")          # Set the variable home by expanding the users set home directory
    print (masa)
    if not os.path.exists(masa+'/dizin'):
        os.makedirs(masa+'/dizin')
except Exception as e:
        print (e)
