from rockyutil.leetcode import *


class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        ans = 0
        chars_cnter = Counter()
        for word in words:
            chars_cnter.update(Counter(word))
        odd_heap_max, even_heap_min = [], []
        for cnt in chars_cnter.values():
            heappush(odd_heap_max if 0b1 == 0b1 & cnt else even_heap_min, -cnt if 0b1 == 0b1 & cnt else cnt)
        for word_len in sorted(len(word) for word in words):
            if 0b1 == 0b1 & word_len:
                if 0 == len(odd_heap_max):
                    if 0 == len(even_heap_min):
                        break
                    even = heappop(even_heap_min)
                    consumption = 1
                    surplus = even - consumption
                    heappush(odd_heap_max, -surplus)
                    heappush(odd_heap_max, -1)
                odd = -heappop(odd_heap_max)
                consumption = min(odd, word_len)
                surplus = odd - consumption
                if 0 < surplus:
                    heappush(even_heap_min, surplus)
                word_len -= consumption
            while 0 < word_len:
                if 0 == len(even_heap_min):
                    if 0 == len(odd_heap_max):
                        break
                    odd = -heappop(odd_heap_max)
                    consumption = min(odd - 1, word_len)
                    surplus = odd - consumption
                    heappush(odd_heap_max, -surplus)
                    if 0 == consumption:
                        break
                    heappush(even_heap_min, consumption)
                even = heappop(even_heap_min)
                consumption = min(even, word_len)
                surplus = even - consumption
                if 0 < surplus:
                    heappush(even_heap_min, surplus)
                word_len -= consumption
            else:
                ans += 1
                continue
            break
        return ans


eg_words = ["a", "a", "caa"]
print(Solution().maxPalindromesAfterOperations(eg_words))
