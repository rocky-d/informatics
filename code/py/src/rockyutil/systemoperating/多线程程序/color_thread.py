from threading import Thread
from time import sleep


class ColorThread(Thread):

    def __init__(self, name: str, color: str, delay: float) -> None:
        super().__init__()
        self.name = name
        self.color = color
        self.delay = delay
        self.count = 0

    def run(self) -> None:
        print(f'\n{self.color}线程“{self.name}”启动\033[0m\n', end = '')
        self.print_color()
        print(f'\n{self.color}线程“{self.name}”结束\033[0m\n', end = '')

    def print_color(self) -> None:
        for _ in range(50):
            self.count += 1
            print(f'{self.color}{self.count}\033[0m,', end = '')
            sleep(self.delay)


if __name__ == '__main__':
    threads = [
        ColorThread('1号红色线程', '\033[91m', 0.1),
        ColorThread('2号绿色线程', '\033[92m', 0.2),
        ColorThread('3号黄色线程', '\033[93m', 0.3),
        ColorThread('4号蓝色线程', '\033[94m', 0.4),
        ColorThread('5号粉色线程', '\033[95m', 0.5)
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
