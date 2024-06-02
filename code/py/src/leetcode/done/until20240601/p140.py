from rockyutil.leetcode import *


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        class TrieNode(object):
            __slots__ = 'val', 'nxts'

            def __init__(self, val: Optional[str], nxts: Dict[str, 'TrieNode']) -> None:
                self.val = val
                self.nxts = nxts

        root = TrieNode(val = None, nxts = {})
        for word in wordDict:
            node = root
            for char in word:
                if char not in node.nxts.keys():
                    node.nxts[char] = TrieNode(val = None, nxts = {})
                node = node.nxts[char]
            node.val = word
        dp = [[[]]]
        n = len(s)
        for i in range(-1, -1 - n, -1):
            dp.insert(0, [])
            node = root
            for j in range(i, 0):
                if s[j] in node.nxts.keys():
                    node = node.nxts[s[j]]
                    if node.val is not None:
                        dp[0] += [[node.val] + words for words in dp[j]]
                else:
                    break
        return [' '.join(words) for words in dp[0]]
