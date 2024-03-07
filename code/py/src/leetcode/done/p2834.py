class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        pivot = target // 2
        lft, rit = min(n, pivot), max(0, n - pivot)
        return (lft * (1 + lft) + rit * (target + target + rit - 1)) // 2 % 1_000_000_007
