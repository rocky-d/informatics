from onlinejudge.leetcode import *


class Solution:
    def smallestNumber(self, pattern: str) -> str:
        nums = []
        idx = 0
        minm = 1
        vis = [None] + [False] * 9
        groups = [(char, len(list(group))) for char, group in groupby(pattern)]
        for i, (char, leng) in enumerate(groups):
            if 'I' == char:
                for _ in range(idx, idx + leng):
                    while vis[minm]:
                        minm += 1
                    vis[minm] = True
                    nums.append(minm)
                idx += leng
            else:  # elif 'D' == char:
                size = leng
                if i + 1 < len(groups):
                    size += groups[i + 1][1]
                else:
                    size += 1
                num = minm + size
                for _ in range(idx, idx + leng):
                    vis[num] = True
                    nums.append(num)
                    num -= 1
                idx += leng
        return ''.join(map(str, nums))


eg_pattern = 'DDD'
print(Solution().smallestNumber(eg_pattern))
