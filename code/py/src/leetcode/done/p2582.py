class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        n2 = n + n
        cnt = time % (n2 - 2)
        return 1 + cnt if cnt < n else n2 - cnt - 1
