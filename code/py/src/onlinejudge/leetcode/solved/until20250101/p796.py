class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and any(s[i:] + s[:i] == goal for i in range(len(s)))
