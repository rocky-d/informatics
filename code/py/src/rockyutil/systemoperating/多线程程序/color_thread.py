from threading import Thread
from time import sleep


class ColorThread(Thread):

    def __init__(self, name: str, color: str, delay: float) -> None:
        super().__init__()
        self.name = name
        self.color = color
        self.delay = delay

    def run(self) -> None:
        print(f'\n“{self.color}{self.name}\033[0m”启动\n', end = '')
        self.print_color()
        print(f'\n“{self.color}{self.name}\033[0m”结束\n', end = '')

    def print_color(self) -> None:
        for i in range(50):
            print(f'{self.color}{i}\033[0m,', end = '')
            sleep(self.delay)


if __name__ == '__main__':
    threads = [
        ColorThread('1号红色线程', '\033[91m', 0.1),
        ColorThread('2号绿色线程', '\033[92m', 0.2),
        ColorThread('3号黄色线程', '\033[93m', 0.3),
        ColorThread('4号蓝色线程', '\033[94m', 0.4),
        ColorThread('5号粉色线程', '\033[95m', 0.5),
    ]

    for thread in threads:
        thread.start()
        thread.join()
