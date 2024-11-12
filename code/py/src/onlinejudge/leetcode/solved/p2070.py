from onlinejudge.leetcode import *


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        ans = [0] * len(queries)
        key = lambda item: item[0]
        items.sort(key=key)
        maxms, maxm = [], 0
        for _, beauty in items:
            maxm = max(maxm, beauty)
            maxms.append(maxm)
        for i, query in enumerate(queries):
            idx = bisect_right(items, query, key=key)
            if 0 == idx:
                continue
            ans[i] = maxms[idx - 1]
        return ans
