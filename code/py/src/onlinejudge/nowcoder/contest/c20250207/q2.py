class Solution:
    def maximumSwap(self, num: str) -> str:
        n = len(num)
        for x in range(n):
            y = max((i for i in range(x + 1, n)), key=lambda x: (num[x], x), default=x)
            if num[x] < num[y]:
                ans = num[:x] + num[y] + num[x + 1 : y] + num[x] + num[y + 1 :]
                break
        else:
            ans = num
        return ans


eg_num = '5'
print(Solution().maximumSwap(eg_num))
