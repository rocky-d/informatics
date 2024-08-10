from onlinejudge.leetcode import *


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        heads = {}

        def find(x: int) -> int:
            if x == heads[x]:
                return x
            heads[x] = find(heads[x])
            return heads[x]

        def union(a: int, b: int) -> None:
            a_head, b_head = find(x = a), find(x = b)
            if a_head != b_head:
                heads[a] = heads[a_head] = b_head

        for num in nums:
            a = num
            if a not in heads.keys():
                heads[a] = a
            for factor in range(2, isqrt(num) + 1):
                times = 0
                while 0 == num % factor:
                    num //= factor
                    times += 1
                if 1 <= times:
                    b = factor
                    if b not in heads.keys():
                        heads[b] = b
                    union(a = a, b = b)
            if 1 < num:
                b = num
                if b not in heads.keys():
                    heads[b] = b
                union(a = a, b = b)
        return max(Counter(find(x = num) for num in nums).values())


eg_nums = [4, 6, 15, 35]
print(Solution().largestComponentSize(eg_nums))
