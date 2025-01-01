class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if len(bin(left)) == len(bin(right)):
            cnt = 0
            while left != right:
                left >>= 1
                right >>= 1
                cnt += 1
            ans = left << cnt
        else:
            ans = 0
        return ans
