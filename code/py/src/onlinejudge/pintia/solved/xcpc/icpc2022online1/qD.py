from bisect import bisect_left, bisect_right
from itertools import combinations


nums = [[] for _ in range(31)]
nums[2].append(2)
for leng in range(3, len(nums)):
    for x in range(2, leng // 2 + 1):
        one_zeros = '1' + '0' * x
        mid = ['0'] * (leng - (x + 2))
        for ls in combinations(range(len(mid)), r=x - 2):
            mid_copy = mid.copy()
            for i in ls:
                mid_copy[i] = '1'
            s = '1' + ''.join(mid_copy) + one_zeros
            nums[leng].append(int(s, base=2))
for ls in nums:
    ls.sort()


def main() -> None:
    l, r = map(int, input().split())

    l_bin, r_bin = bin(l)[2:], bin(r)[2:]
    for leng in range(len(l_bin), len(r_bin) + 1):
        ls = nums[leng]
        lft, rit = bisect_left(ls, l), bisect_right(ls, r)
        if lft < rit:
            res = ls[lft]
            break
    else:
        res = -1
    print(res)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
