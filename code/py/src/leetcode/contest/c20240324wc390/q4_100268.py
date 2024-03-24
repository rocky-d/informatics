from rockyutil.leetcode import *


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        ans = []

        class TrieNode(object):
            def __init__(self, char, children, idx, depth):
                self.char = char
                self.children = children
                self.idx = idx
                self.depth = depth

        root = TrieNode(char = '', children = {}, idx = None, depth = inf)

        def build(node: TrieNode, i: int) -> None:
            if -1 == i:
                if node.idx is None:
                    node.idx = idx
                return
            node.depth = min(node.depth, i + 1)
            if word[i] in node.children:
                build(node.children[word[i]], i - 1)
            else:
                node.children[word[i]] = TrieNode(char = word[i], children = {}, idx = None, depth = i)
                build(node.children[word[i]], i - 1)

        for idx, word in enumerate(wordsContainer):
            build(node = root, i = len(word) - 1)

        def find_leaf(node: TrieNode) -> int:
            if node.idx is not None:
                return node.idx
            min_depth = inf, None
            for child in node.children.values():
                if child.depth < min_depth[0]:
                    min_depth = child.depth, child
            return find_leaf(min_depth[1])

        def dfs(node: TrieNode, i: int):
            if i == -1:
                if node.idx is not None:
                    ans.append(node.idx)
                else:
                    min_depth = inf, None
                    for child in node.children.values():
                        if child.depth < min_depth[0]:
                            min_depth = child.depth, child
                    ans.append(find_leaf(min_depth[1]))
                return
            if query[i] in node.children:
                dfs(node.children[query[i]], i - 1)
            else:
                if node.idx is not None:
                    ans.append(node.idx)
                else:
                    min_depth = inf, None
                    for child in node.children.values():
                        if child.depth < min_depth[0]:
                            min_depth = child.depth, child
                    ans.append(find_leaf(min_depth[1]))

        for query in wordsQuery:
            dfs(node = root, i = len(query) - 1)
        return ans


eg_wordsContainer = ['bcbdbcdbda', 'bdcaaccca', 'baaccadcba', 'cdacda', 'cddabdaaab']
eg_wordsQuery = ['a']
print(Solution().stringIndices(eg_wordsContainer, eg_wordsQuery))
