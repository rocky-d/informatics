import threading
import time


class Semaphore(object):
    def __init__(self):
        self.lock = threading.Lock()
        self.lock.acquire()

    def p(self):
        self.lock.acquire()

    def v(self):
        self.lock.release()


class Driver(threading.Thread):

    def __init__(self, door: Semaphore, stop: Semaphore):
        super().__init__()
        self.door = door
        self.stop = stop

    def run(self):
        while True:
            self.door.p()  # 等待关门

            print('\033[92mDriver: 行车\n', end = '')
            time.sleep(2)
            print('\033[92mDriver: 停车\n', end = '')
            time.sleep(2)

            self.stop.v()  # 告知Conductor已停车


class Conductor(threading.Thread):

    def __init__(self, door: Semaphore, stop: Semaphore):
        super().__init__()
        self.door = door
        self.stop = stop

    def run(self):
        while True:
            print('\033[93mConductor: 等待乘客上下车\n', end = '')
            time.sleep(0.5)
            print('\033[93mConductor: 关门\n', end = '')
            time.sleep(0.5)

            self.door.v()  # 告知Driver已关门

            print('\033[93mConductor: 售票\n', end = '')
            time.sleep(0.5)

            self.stop.p()  # 等待停车

            print('\033[93mConductor: 开门\n', end = '')
            time.sleep(0.5)


if __name__ == '__main__':
    door, stop = Semaphore(), Semaphore()

    conductor = Conductor(door = door, stop = stop)
    driver = Driver(door = door, stop = stop)

    conductor.start()
    driver.start()

    conductor.join()
    driver.join()
