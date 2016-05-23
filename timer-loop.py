import threading

def bang():
    threading.Timer(5.0,bang).start()
    print("boom")
def main():
    bang()

if __name__=='__main__':
    main()
