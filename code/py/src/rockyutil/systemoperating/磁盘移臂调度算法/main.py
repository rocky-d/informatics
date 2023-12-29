from bisect import bisect_left
from random import randint


class MovingArm(object):

    def __init__(self, total_cylinders: int, cylinders: list[int], start: int, show_details: bool) -> None:
        self.total_cylinders: int = total_cylinders
        self.cylinders: list[int] = cylinders
        self.start: int = start
        self.show_details: bool = show_details

    def __print(self, *args, **kwargs) -> None:
        if self.show_details:
            print(*args, **kwargs)

    def first_come_first_served(self) -> int:
        distance = 0
        sequence = []
        current = self.start
        for cylinder in self.cylinders:
            distance += abs(current - cylinder)
            sequence.append(cylinder)
            current = cylinder
        self.__print(sequence)
        self.__print()
        return distance

    def shortest_seek_time_first(self) -> int:
        distance = 0
        sequence = []
        current = self.start
        cylinders = [(cylinder, i) for i, cylinder in enumerate(self.cylinders)]
        while 0 < len(cylinders):
            cylinders.sort(key = lambda x: (abs(current - x[0]), x[1]))
            cylinder = cylinders.pop(0)[0]
            distance += abs(current - cylinder)
            sequence.append(cylinder)
            current = cylinder
        self.__print(sequence)
        self.__print()
        return distance

    def uni_scan(self) -> int:
        distance = 0
        sequence = []
        current = self.start
        cylinders = [(cylinder, i) for i, cylinder in enumerate(self.cylinders)]
        if min(self.cylinders) < current:
            gap = True
            cylinders.append((self.total_cylinders, len(self.cylinders)))
            cylinders.append((1, len(self.cylinders)))
        else:
            gap = False
        cylinders.sort(key = lambda x: (x[0], x[1]))
        cylinders = [cylinder for cylinder, i in cylinders]
        pivot = bisect_left(cylinders, current)
        cylinders = cylinders[pivot:] + cylinders[:pivot]
        for cylinder in cylinders:
            distance += abs(current - cylinder)
            sequence.append(cylinder)
            current = cylinder
        self.__print(sequence)
        self.__print()
        return distance - self.total_cylinders + 2 if gap else distance

    def double_scan(self) -> int:
        distance = 0
        sequence = []
        current = self.start
        cylinders = [(cylinder, i) for i, cylinder in enumerate(self.cylinders)]
        if min(self.cylinders) < current:
            cylinders.append((self.total_cylinders, len(self.cylinders)))
        cylinders.sort(key = lambda x: (x[0], x[1]))
        cylinders = [cylinder for cylinder, i in cylinders]
        pivot = bisect_left(cylinders, current)
        cylinders = cylinders[pivot:] + cylinders[:pivot][::-1]
        for cylinder in cylinders:
            distance += abs(current - cylinder)
            sequence.append(cylinder)
            current = cylinder
        self.__print(sequence)
        self.__print()
        return distance

    def elevator(self) -> int:
        distance = 0
        sequence = []
        current = self.start
        cylinders = [(cylinder, i) for i, cylinder in enumerate(self.cylinders)]
        cylinders.sort(key = lambda x: (x[0], x[1]))
        cylinders = [cylinder for cylinder, i in cylinders]
        pivot = bisect_left(cylinders, current)
        cylinders = cylinders[pivot:] + cylinders[:pivot][::-1]
        for cylinder in cylinders:
            distance += abs(current - cylinder)
            sequence.append(cylinder)
            current = cylinder
        self.__print(sequence)
        self.__print()
        return distance


def random_cylinders(max_cylinder: int, len_cylinders: int, show_details: bool) -> list[int]:
    cylinders = []
    for _ in range(len_cylinders):
        cylinders.append(randint(a = 1, b = max_cylinder))
    if show_details:
        print('柱面调用顺序：')
        print(f"{cylinders = }")
    return cylinders


if __name__ == '__main__':
    movingArm = MovingArm(
        total_cylinders = int(input('磁盘柱面数 > ')),
        # cylinders = [11, 9, 17, 11, 22, 9, 11],
        cylinders = random_cylinders(
            max_cylinder = int(input('最大调用柱面数 > ')),
            len_cylinders = int(input('柱面随机调用次数 > ')),
            show_details = bool(input('输入任何内容以展示柱面调用顺序（直接按下回车键以忽略柱面调用顺序） > '))
        ),
        start = int(input()),
        show_details = bool(input('输入任何内容以展示移动臂移动过程（直接按下回车键以忽略移动臂移动过程） > '))
    )
    print('移动臂移动过程，移动距离：')
    print(f"{movingArm.first_come_first_served() = }")
    print(f"{movingArm.shortest_seek_time_first() = }")
    print(f"{movingArm.uni_scan() = }")
    print(f"{movingArm.double_scan() = }")
    print(f"{movingArm.elevator() = }")
