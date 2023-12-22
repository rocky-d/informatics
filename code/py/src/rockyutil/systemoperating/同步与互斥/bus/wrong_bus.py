import time
from threading import Thread, Lock

door_lock, stop_lock = Lock(), Lock()


class Driver(Thread):
    def run(self) -> None:
        while True:
            door_lock.acquire()

            print('\033[92mDriver: 行车\n', end = '')
            time.sleep(2)
            print('\033[92mDriver: 停车\n', end = '')
            time.sleep(2)

            if stop_lock.locked():
                stop_lock.release()


class Conductor(Thread):
    def run(self) -> None:
        while True:
            print('\033[93mConductor: 等待乘客上下车\n', end = '')
            time.sleep(0.5)
            print('\033[93mConductor: 关门\n', end = '')
            time.sleep(0.5)

            if door_lock.locked():
                door_lock.release()

            print('\033[93mConductor: 售票\n', end = '')
            time.sleep(0.5)

            stop_lock.acquire()

            print('\033[93mConductor: 开门\n', end = '')
            time.sleep(0.5)


def main() -> None:
    driver = Driver()
    conductor = Conductor()

    driver.start()
    conductor.start()

    # driver.join()
    # conductor.join()


if __name__ == '__main__':
    main()

# typedef int Semaphore;
#
# Semaphore door=0, stop=0;
#
# // 下列进程Driver和Conductor并发执行
# process Driver(void) {
#     while (1) {
#         P(door);  // 等待关门
#         { 行车; }
#         { 停车; }
#         V(stop);  // 告知Conductor已停车
#     }
# }
# process Conductor(void) {
#     while (1) {
#         { 关门; }
#         V(door);  // 告知Driver已关门
#         { 售票; }
#         P(stop);  // 等待停车
#         { 开门; }
#     }
# }
