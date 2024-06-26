class Solution:
    def smallestString(self, s: str) -> str:
        dct = {'a': 'z', 'b': 'a', 'c': 'b', 'd': 'c', 'e': 'd', 'f': 'e', 'g': 'f', 'h': 'g', 'i': 'h', 'j': 'i',
               'k': 'j', 'l': 'k', 'm': 'l', 'n': 'm', 'o': 'n', 'p': 'o', 'q': 'p', 'r': 'q', 's': 'r', 't': 's',
               'u': 't', 'v': 'u', 'w': 'v', 'x': 'w', 'y': 'x', 'z': 'y'}
        if 'a' == s[0]:
            if 1 == len(frozenset(s)):
                ans = s[:-1] + 'z'
            else:
                idx = s.find('a', 1)
                if -1 == idx:
                    ans = 'a' + ''.join(map(lambda char: dct[char], s[1:]))
                else:
                    ans = 'a' + ''.join(map(lambda char: dct[char], s[1:idx])) + s[idx:]
        else:
            idx = s.find('a')
            if -1 == idx:
                ans = ''.join(map(lambda char: dct[char], s))
            else:
                ans = ''.join(map(lambda char: dct[char], s[:idx])) + s[idx:]
        return ans
