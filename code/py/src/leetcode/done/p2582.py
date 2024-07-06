class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        n2 = n + n
        time %= (n2 - 2)
        return 1 + time if time < n else n2 - time - 1
