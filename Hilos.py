import threading

def cuenta(n , name):
    count = n
    while count < 10:
        print(name, " : ", count)
        print("...")
        count += 1

t1 = threading.Thread(target=cuenta, args=(1, 'Hilo 1',) )
t2 = threading.Thread(target=cuenta, args=(2, 'Hilo 2',) )
t3 = threading.Thread(target=cuenta, args=(3, 'Hilo 3',) )

t1.start()
t2.start()
t3.start()