from bisect import bisect_left
from random import randint


class MovingArm(object):

    def __init__(self, total_cylinders: int, cylinders: list[int], start: int, decreasing: bool, show_details: bool) -> None:
        self.total_cylinders: int = total_cylinders
        self.cylinders: list[int] = cylinders
        self.start: int = start
        self.increasing: bool = not decreasing
        self.show_details: bool = show_details

    def __print(self, *args, **kwargs) -> None:
        if self.show_details:
            print(*args, **kwargs)

    def first_come_first_served(self) -> int:
        distance: int = 0
        sequence: list[int] = []
        current: int = self.start
        for cylinder in self.cylinders:
            distance += abs(current - cylinder)
            sequence.append(cylinder)
            current = cylinder
        self.__print(sequence)
        return distance

    def shortest_seek_time_first(self) -> int:
        distance: int = 0
        sequence: list[int] = []
        current: int = self.start
        cylinders = [(cylinder, i) for i, cylinder in enumerate(self.cylinders)]
        while 0 < len(cylinders):
            cylinders.sort(key = lambda x: (abs(current - x[0]), x[1]))
            cylinder = cylinders.pop(0)[0]
            distance += abs(current - cylinder)
            sequence.append(cylinder)
            current = cylinder
        self.__print(sequence)
        return distance

    def uni_scan(self) -> int:
        distance: int = 0
        sequence: list[int] = []
        current: int = self.start
        cylinders = [(cylinder, i) for i, cylinder in enumerate(self.cylinders)]
        if min(self.cylinders) < current:
            gap = True
            cylinders.append((self.total_cylinders, len(self.cylinders)))
            cylinders.append((1, len(self.cylinders)))
        else:
            gap = False
        cylinders = [cylinder for cylinder, i in sorted(cylinders, key = lambda x: (x[0], x[1]))]
        pivot = bisect_left(cylinders, current)
        cylinders = cylinders[pivot:] + cylinders[:pivot]
        for cylinder in cylinders:
            distance += abs(current - cylinder)
            sequence.append(cylinder)
            current = cylinder
        self.__print(sequence)
        return distance - self.total_cylinders + 2 if gap else distance

    def double_scan(self) -> int:
        distance: int = 0
        sequence: list[int] = []
        current: int = self.start
        cylinders = [(cylinder, i) for i, cylinder in enumerate(self.cylinders)]
        if min(self.cylinders) < current:
            cylinders.append((self.total_cylinders if self.increasing else 1, len(self.cylinders)))
        cylinders = [cylinder for cylinder, i in sorted(cylinders, key = lambda x: (x[0], x[1]))]
        pivot = bisect_left(cylinders, current)
        cylinders = cylinders[pivot:] + cylinders[:pivot][::-1] if self.increasing else cylinders[:pivot][::-1] + cylinders[pivot:]
        for cylinder in cylinders:
            distance += abs(current - cylinder)
            sequence.append(cylinder)
            current = cylinder
        self.__print(sequence)
        return distance

    def elevator(self) -> int:
        distance: int = 0
        sequence: list[int] = []
        current: int = self.start
        cylinders = [(cylinder, i) for i, cylinder in enumerate(self.cylinders)]
        cylinders = [cylinder for cylinder, i in sorted(cylinders, key = lambda x: (x[0], x[1]))]
        pivot = bisect_left(cylinders, current)
        cylinders = cylinders[pivot:] + cylinders[:pivot][::-1] if self.increasing else cylinders[:pivot][::-1] + cylinders[pivot:]
        for cylinder in cylinders:
            distance += abs(current - cylinder)
            sequence.append(cylinder)
            current = cylinder
        self.__print(sequence)
        return distance


def random_cylinders(max_cylinder: int, len_cylinders: int, show_details: bool) -> list[int]:
    cylinders: list[int] = []
    for _ in range(len_cylinders):
        cylinders.append(randint(a = 1, b = max_cylinder))
    if show_details:
        print()
        print('柱面调用顺序：')
        print(f"{cylinders = }")
    return cylinders


if __name__ == '__main__':
    movingArm = MovingArm(
        total_cylinders = int(input('\n磁盘柱面数 > ')),
        # cylinders = [11, 9, 17, 11, 22, 9, 11],
        # cylinders = [86, 147, 91, 177, 94, 150, 102, 175, 130],
        cylinders = random_cylinders(
            max_cylinder = int(input('\n最大调用柱面 > ')),
            len_cylinders = int(input('\n柱面随机调用次数 > ')),
            show_details = bool(input('\n直接按下回车键以忽略/输入任何内容以展示 柱面调用顺序 > '))
        ),
        start = int(input('\n移动臂起始所在柱面 > ')),
        decreasing = bool(input('\n移动臂正在向 内/外（最大号柱面/1号柱面） 扫描（直接按下回车以选择向内，输入任何内容以选择向外） > ')),
        show_details = bool(input('\n直接按下回车键以忽略/输入任何内容以展示 移动臂移动过程 > '))
    )
    print()
    print('移动臂移动过程，移动距离：')
    print(f"{movingArm.first_come_first_served() = }\n")
    print(f"{movingArm.shortest_seek_time_first() = }\n")
    print(f"{movingArm.uni_scan() = }\n")
    print(f"{movingArm.double_scan() = }\n")
    print(f"{movingArm.elevator() = }\n")
