from onlinejudge.leetcode import *


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(lambda: [])
        for s in strs:
            anagrams[frozenset(Counter(s).items())].append(s)
        return list(anagrams.values())


eg_strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
print(Solution().groupAnagrams(eg_strs))
