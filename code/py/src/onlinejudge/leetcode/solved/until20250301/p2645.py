class Solution:
    def addMinimum(self, word: str) -> int:
        ans = 0
        stack = []
        for char in word:
            if 'a' == char:
                if 0 == len(stack):
                    stack.append('a')
                elif 1 == len(stack):
                    if 'a' == stack[0]:
                        ans += 2
                    else:
                        ans += 2
                        stack[0] = 'a'
                else:
                    ans += 1
                    stack.pop(1)
            elif 'b' == char:
                if 0 == len(stack):
                    stack.append('b')
                elif 1 == len(stack):
                    if 'a' == stack[0]:
                        stack.append('b')
                    else:
                        ans += 2
                else:
                    ans += 1
                    stack.pop(0)
            else:
                if 0 == len(stack):
                    ans += 2
                elif 1 == len(stack):
                    ans += 1
                    stack.pop(0)
                else:
                    stack.pop(0)
                    stack.pop(0)
        else:
            if 1 == len(stack):
                ans += 2
            elif 2 == len(stack):
                ans += 1
        return ans
