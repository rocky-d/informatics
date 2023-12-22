import threading
import time


class Semaphore:
    def __init__(self):
        self.lock = threading.Lock()
        self.value = 0

    def p(self):
        self.lock.acquire()
        while self.value <= 0:
            self.lock.release()
            self.lock.acquire()
        self.value -= 1
        self.lock.release()

    def v(self):
        self.lock.acquire()
        self.value += 1
        self.lock.release()


class Driver(threading.Thread):
    def __init__(self, door, stop):
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
    def __init__(self, door, stop):
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
    dor, stp = Semaphore(), Semaphore()

    Driver(dor, stp).start()
    Conductor(dor, stp).start()
