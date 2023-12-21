from rockyutil.leetcode import *


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_dict = {}
        for char in chars:
            chars_dict[char] = 1 + chars_dict.get(char, 0)
        ans = 0
        for word in words:
            new_dict = {}
            for char in word:
                new_dict[char] = 1 + new_dict.get(char, 0)
                if chars_dict.get(char, 0) < new_dict[char]:
                    break
            else:
                ans += len(word)
        return ans
