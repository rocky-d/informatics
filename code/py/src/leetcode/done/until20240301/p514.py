class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        ring_len = len(ring)
        dp = {0: 0}
        for char in key:
            dp_last, dp = dp, {}
            for index, count in dp_last.items():
                ring_rotated = ring[index:] + ring[:index]
                right_steps = ring_rotated.index(char)
                left_steps = 1 + ring_rotated[::-1].index(char)
                right_index = (index + right_steps) % ring_len
                left_index = (index - left_steps + ring_len) % ring_len
                dp[right_index] = min(dp.get(right_index, 10_001), count + right_steps + 1)
                dp[left_index] = min(dp.get(left_index, 10_001), count + left_steps + 1)
        return min(dp.values())


eg_ring = 'nyngl'
eg_key = 'ynl'
print(Solution().findRotateSteps(ring = eg_ring, key = eg_key))
