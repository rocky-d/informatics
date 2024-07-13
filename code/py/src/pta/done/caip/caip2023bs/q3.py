from collections import Counter


def main() -> None:
    for _ in range(int(input())):
        nums = map(int, input().split())
        cnter = Counter(nums)
        if 1 == len(cnter):
            print('0 0 1')  # 5/7776
        elif 2 == len(cnter):
            cnts = sorted(cnter.values())
            if 4 == cnts[-1]:
                print('1 1 6')  # 30/7776
            else:  # elif 3 == cnts[-1]:
                print('2 1 3')  # 30/7776
        elif 3 == len(cnter):
            cnts = sorted(cnter.values())
            if 3 == cnts[-1]:
                print('2 4 9')  # 120/7776
            else:  # elif 2 == cnts[-1]:
                print('3 4 9')  # 120/7776
        elif 4 == len(cnter):
            print('3 13 18')  # 360/7776
        else:  # elif 5 == len(cnter):
            nums = sorted(cnter.keys())
            if 2 == nums[0] and 6 == nums[-1]:
                ...
            elif 1 == nums[0] and 5 == nums[-1]:
                ...
            else:
                ...


if __name__ == '__main__':
    main()
