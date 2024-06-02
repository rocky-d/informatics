from bisect import *
from collections import Counter


def main() -> None:
    n = int(input())
    matrix = (input() for _ in range(n))

    ans = []
    digits_hex = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
                  'C': 12, 'D': 13, 'E': 14, 'F': 15, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    cnter = Counter()
    back_hex = {}
    img = []
    for row in matrix:
        img.append([])
        for i in range(0, len(row), 2):
            num = 16 * digits_hex[row[i]] + digits_hex[row[i + 1]]
            img[-1].append(num)
            cnter[num] += 1
            back_hex[num] = row[i].upper() + row[i + 1].upper()
    nums, cnts = [], []
    for num, cnt in sorted(cnter.items(), key = lambda item: (-item[1], item[0]))[:16]:
        nums.append(num), cnts.append(cnt)
    print(*(back_hex[nums[i]] for i in range(16)), sep = '')

    new_hex = {nums[i]: h for i, h in enumerate('0123456789ABCDEF')}
    idxes = {num: i for i, num in enumerate(nums)}
    nums.sort()
    for row in img:
        ans.append('')
        for num in row:
            index = bisect_left(nums, num)
            if index < 16 and nums[index] == num:
                ans[-1] += new_hex[nums[index]]
            else:
                if 0 == index:
                    ans[-1] += new_hex[nums[0]]
                elif 16 == index:
                    ans[-1] += new_hex[nums[15]]
                else:
                    if abs(nums[index - 1] - num) < abs(nums[index] - num):
                        ans[-1] += new_hex[nums[index - 1]]
                    elif abs(nums[index] - num) < abs(nums[index - 1] - num):
                        ans[-1] += new_hex[nums[index]]
                    else:
                        if idxes[nums[index - 1]] < idxes[nums[index]]:
                            ans[-1] += new_hex[nums[index - 1]]
                        else:
                            ans[-1] += new_hex[nums[index]]
    print(*ans, sep = '\n')


if __name__ == '__main__':
    main()
