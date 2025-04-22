from onlinejudge.leetcode import *


class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        ans = 0
        dp = [0] + [0] * n
        dp[1] += 1
        for leng in range(1, 1 + n):
            dp_lst, dp = dp, [0] + [0] * n
            for num, cnt in enumerate(dp):
                ...


'''
1

-----

1
2
3
4
5
6
7
8

------

1 1
1 2
1 3
1 4
1 5
1 6
1 7
1 8

2 2
2 4
2 6
2 8

3 3
3 6

4 4
4 8

5 5

6 6

7 7

8 8

------

1 1 1
1 1 2
1 1 3
1 1 4
1 1 5
1 1 6
1 1 7
1 1 8
1 2 2
1 2 4
1 2 6
1 2 8
1 3 3
1 3 6
1 4 4
1 4 8
1 5 5
1 6 6
1 7 7
1 8 8

2 2 2
2 2 4
2 2 6
2 2 8
2 4 4
2 4 8

3 3 3
3 3 6
3 6 6

4 4 4
4 4 8
4 8 8

5 5 5
6 6 6
7 7 7
8 8 8
'''
