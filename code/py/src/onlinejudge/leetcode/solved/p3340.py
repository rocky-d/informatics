class Solution:
    def isBalanced(self, num: str) -> bool:
        return sum(map(int, num[0::2])) == sum(map(int, num[1::2]))
