from rockyutil.leetcode import *


class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        ans = 0
        chars_cnter = Counter()
        for word in words:
            for char in word:
                chars_cnter[char] += 1
        odd_heap_max, evens = [], deque()
        for cnt in chars_cnter.values():
            if 0b1 == 0b1 & cnt:
                heappush(odd_heap_max, -cnt)
            else:
                evens.append(cnt)
        for word_len in sorted(len(word) for word in words):
            if 0b1 == 0b1 & word_len:
                if 0 == len(odd_heap_max):
                    if 0 == len(evens):
                        break
                    even = evens.pop()
                    consumption = 1
                    surplus = even - consumption
                    heappush(odd_heap_max, -surplus)
                    heappush(odd_heap_max, -1)
                odd = -heappop(odd_heap_max)
                consumption = min(odd, word_len)
                surplus = odd - consumption
                if 0 < surplus:
                    evens.append(surplus)
                word_len -= consumption
            while 0 < word_len:
                if 0 == len(evens):
                    if 0 == len(odd_heap_max):
                        break
                    odd = -heappop(odd_heap_max)
                    consumption = min(odd - 1, word_len)
                    surplus = odd - consumption
                    heappush(odd_heap_max, -surplus)
                    if 0 == consumption:
                        break
                    evens.append(consumption)
                even = evens.pop()
                consumption = min(even, word_len)
                surplus = even - consumption
                if 0 < surplus:
                    evens.append(surplus)
                word_len -= consumption
            else:
                ans += 1
                continue
            break
        return ans


eg_words = ['a', 'a', 'caa']
print(Solution().maxPalindromesAfterOperations(eg_words))
