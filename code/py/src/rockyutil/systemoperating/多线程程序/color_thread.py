import time
from threading import *


class ColorThread(Thread):
    char = '0'

    def __init__(self, name: str, color: str, delay: float) -> None:
        super().__init__()
        self.name = name
        self.color = color
        self.delay = delay

    def run(self) -> None:
        print(f'\n{self.color}线程“{self.name}”启动\033[0m\n', end = '')
        self.print_color()
        print(f'\n{self.color}线程“{self.name}”结束\033[0m\n', end = '')

    def print_color(self) -> None:
        for _ in range(50):
            print(f'{self.color}{ColorThread.char}\033[0m,', end = '')
            time.sleep(self.delay)


if __name__ == '__main__':
    thread1 = ColorThread('1号粉色线程', '\033[95m', 0.5)
    thread2 = ColorThread('2号蓝色线程', '\033[94m', 0.4)
    thread3 = ColorThread('3号黄色线程', '\033[93m', 0.3)
    thread4 = ColorThread('4号绿色线程', '\033[92m', 0.2)
    thread5 = ColorThread('5号红色线程', '\033[91m', 0.1)

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
