from onlinejudge.leetcode import *


class Solution:
    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
        idxes = [i for i in range(2) if 1 == nums[i]]
        sum3 = sum3_tmp = nums[0] + nums[1]
        oneone = 1 == nums[0] == nums[1]
        for i in range(2, len(nums)):
            if 1 == nums[i]:
                idxes.append(i)
            sum3_tmp += nums[i]
            sum3 = max(sum3, sum3_tmp)
            sum3_tmp -= nums[i - 2]
            if not oneone:
                oneone = 1 == nums[i - 1] == nums[i]
        if k <= sum3:  # k∈[1, sum3]
            ans = k if 2 == k and not oneone else k - 1
        elif k <= sum3 + maxChanges:  # k∈[sum3 + 1, sum3 + maxChanges]
            if 0 == sum3:
                ans = 2 * k
            elif 1 == sum3:
                ans = 2 * (k - 1)
            elif 2 == sum3:
                ans = (1 if oneone else 2) + 2 * (k - 2)
            else:  # elif 3 == sum3:
                ans = 2 + 2 * (k - 3)
        else:  # k∈[sum3 + maxChanges + 1, nums.count(1) + maxChanges]
            prefs = list(accumulate(idxes, initial = 0))
            window_len = k - maxChanges
            lft, rit = window_len // 2, (window_len - 1) // 2
            diff = lft - rit
            ans = 2 * maxChanges + min(diff * idxes[i] + prefs[i - lft] - prefs[i] - prefs[i + 1] + prefs[i + 1 + rit] for i in range(lft, len(idxes) - rit))
        return ans


eg_nums = [1, 1, 0, 0, 0, 1, 1, 0, 0, 1]
eg_k = 3
eg_maxChanges = 1
print(Solution().minimumMoves(eg_nums, eg_k, eg_maxChanges))
