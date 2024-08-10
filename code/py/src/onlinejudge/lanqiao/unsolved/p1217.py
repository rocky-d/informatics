def cube_root(num: int) -> float:
    if 0 == num:
        return 0
    for x in (1, 10, 100, 1000):
        left = 0
        right = num + 1
        mid = None
        while left < right:
            mid = (left + right) / 2
            mid_cube = (mid / x) ** 3
            if num < mid_cube:
                right = mid
            elif num > mid_cube:
                left = mid + 1 / x
            else:  # num == mid_cube
                return mid

    return mid


def main():
    t = int(input())
    for _ in range(t):
        # print('{:.3f}'.format(int(input()) ** (1 / 3)))
        # print(f'{int(input()) ** (1 / 3):.3f}')
        print(cube_root(int(input())))


if __name__ == '__main__':
    main()
