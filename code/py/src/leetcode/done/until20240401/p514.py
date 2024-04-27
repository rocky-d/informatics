class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        dp = {0: 0}
        for char in key:
            dp_lst, dp = dp, {}
            for idx, cnt in dp_lst.items():
                ring_rotated = ring[idx:] + ring[:idx]
                rit_steps = ring_rotated.index(char)
                lft_steps = 1 + ring_rotated[::-1].index(char)
                rit_idx = (idx + rit_steps) % n
                lft_idx = (idx - lft_steps + n) % n
                dp[rit_idx] = min(dp.get(rit_idx, 10_001), cnt + rit_steps + 1)
                dp[lft_idx] = min(dp.get(lft_idx, 10_001), cnt + lft_steps + 1)
        return min(dp.values())


eg_ring = 'nyngl'
eg_key = 'ynl'
print(Solution().findRotateSteps(eg_ring, eg_key))
