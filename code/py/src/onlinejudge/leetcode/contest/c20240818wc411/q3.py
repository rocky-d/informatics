class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        initials = [None, '987654321', '8642', '987654321', '8642', '5', '8642', '987654321', '8642', '987654321']
        mid = n + 1 >> 1
        ls = [''] * n

        def dfs(i: int) -> bool:
            if i == mid:
                return 0 == int(''.join(ls)) % k
            i1 = i + 1
            for digit in initials[k] if 0 == i else '9876543210':
                ls[i] = ls[n - 1 - i] = digit
                if dfs(i1):
                    res = True
                    break
            else:
                res = False
            return res

        dfs(i = 0)
        return ''.join(ls)
