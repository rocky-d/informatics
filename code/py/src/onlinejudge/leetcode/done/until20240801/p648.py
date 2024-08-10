from onlinejudge.leetcode import *


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        class TrieNode(object):
            def __init__(self, val, nxts):
                self.val = val
                self.nxts = nxts

        root = TrieNode(val = False, nxts = {})
        for word in dictionary:
            node = root
            for char in word:
                if char not in node.nxts.keys():
                    node.nxts[char] = TrieNode(val = False, nxts = {})
                node = node.nxts[char]
            node.val = True
        words = []
        for word in sentence.split(' '):
            node = root
            for i, char in enumerate(word, 1):
                if char not in node.nxts.keys():
                    i = len(word)
                    break
                node = node.nxts[char]
                if node.val:
                    break
            words.append(word[:i])
        return ' '.join(words)
