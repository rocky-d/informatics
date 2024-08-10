import threading
import time

customers = threading.Semaphore(0)
barbers = threading.Semaphore(0)
mutex = threading.Lock()
wait_customer = 0
CHAIRS = 5

def customer():
    print('... Customer''s process')
    global wait_customer
    global CHAIRS
    global customers,barbers,mutex

    time.sleep(1)
    mutex.acquire()
    if (wait_customer<CHAIRS):
        wait_customer+=1
        print ('''Customers' number is ''',wait_customer)
        customers.release()
        mutex.release()
        barbers.acquire()
    else:
        print ('Too many customers !')
        mutex.release()

def barber():
    print( '... Barber''s process')
    global wait_customer
    global CHAIRS
    global customers,barbers,mutex
    while(1):
        if(wait_customer==0):
            print ('Barber: I am sleeping now...')
        time.sleep(1)
        customers.acquire()
        mutex.acquire()
        wait_customer-=1
        barbers.release()
        mutex.release()
        cut_hair()

def cut_hair():
    print('Barber:  I am cutting the customer''s hair...')
    time.sleep(2)
    print( 'Barber:  done.')

if __name__ == "__main__":
    t1 = threading.Thread(target=barber)
    t1.start()
    t1.join(1)
    while(1):
        try:
            time.sleep(0.5)
            t2 = threading.Thread(target=customer)
            t2.start()
            t2.join(1)
        except  Exception as e:
                print ('Program terminated .',e)
