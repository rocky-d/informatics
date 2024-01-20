class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t_list = list(t)
        for char in s:
            t_list.remove(char)
        return t_list[0]
