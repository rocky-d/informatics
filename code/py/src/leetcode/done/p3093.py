from rockyutil.leetcode import *


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        ans = []

        class TrieNode(object):
            def __init__(self, val1: int, val2: int, children: Dict[str, 'TrieNode']) -> None:
                self.val1 = val1
                self.val2 = val2
                self.children = children

        def add(node: TrieNode, w: int, c: int) -> None:
            if len(word) < node.val1:
                node.val1 = len(word)
                node.val2 = w
            if c < 0:
                return
            char = word[c]
            if char not in node.children.keys():
                node.children[char] = TrieNode(val1 = 5001, val2 = 10000, children = {})
            add(node.children[char], w, c - 1)

        root = TrieNode(val1 = 5001, val2 = 10000, children = {})
        for w, word in enumerate(wordsContainer):
            add(node = root, w = w, c = len(word) - 1)

        def dfs(node: TrieNode, word: str, c: int) -> int:
            if c < 0:
                return node.val2
            char = word[c]
            return dfs(node.children[char], word, c - 1) if char in node.children.keys() else node.val2

        for word in wordsQuery:
            ans.append(dfs(node = root, word = word, c = len(word) - 1))
        return ans


eg_wordsContainer = ['abcd', 'bcd', 'xbcd']
eg_wordsQuery = ['cd', 'bcd', 'xyz']
print(Solution().stringIndices(eg_wordsContainer, eg_wordsQuery))
