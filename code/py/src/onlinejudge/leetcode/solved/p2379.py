class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = cnt = sum(1 for i in range(k) if 'W' == blocks[i])
        for lft, rit in zip(range(len(blocks) - k), range(k, len(blocks))):
            if 'W' == blocks[rit]:
                cnt += 1
            if 'W' == blocks[lft]:
                cnt -= 1
            ans = min(ans, cnt)
        return ans
