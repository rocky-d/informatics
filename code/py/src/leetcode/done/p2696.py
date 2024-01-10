class Solution:
    def minLength(self, s: str) -> int:
        ans = len(s)
        stack = []
        for char in s:
            if 'A' == char or 'C' == char:
                stack.append(char)
                continue
            elif 'B' == char:
                if 0 < len(stack) and 'A' == stack[-1]:
                    stack.pop(-1)
                    ans -= 2
                    continue
            elif 'D' == char:
                if 0 < len(stack) and 'C' == stack[-1]:
                    stack.pop(-1)
                    ans -= 2
                    continue
            stack.clear()
        return ans


eg_s = 'ABFCACDB'
print(Solution().minLength(s = eg_s))
