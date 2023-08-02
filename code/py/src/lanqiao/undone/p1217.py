def cube_root(num):
    left = 0
    right = num + 1
    mid = -1
    while left < right:
        mid = (left + right) / 2
        if mid ** 3 >= num:
            right = mid
        else:
            left = mid + 1

    return mid


def main():
    t = int(input())
    for _ in range(t):
        # print('{:.3f}'.format(int(input()) ** (1 / 3)))
        # print(f'{int(input()) ** (1 / 3):.3f}')
        print(cube_root(int(input())))


if __name__ == '__main__':
    main()
