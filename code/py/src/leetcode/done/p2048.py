class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        while True:
            n += 1
            n_str = str(n)
            for digit in set(n_str):
                if int(digit) != n_str.count(digit):
                    break
            else:
                ans = n
                break
        return ans
