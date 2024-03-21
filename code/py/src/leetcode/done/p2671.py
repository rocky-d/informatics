from rockyutil.leetcode import *


class FrequencyTracker:
    def __init__(self) -> None:
        self.freq = Counter()
        self.freq_cnter = Counter()

    def add(self, number: int) -> None:
        self.freq_cnter[self.freq[number]] -= 1
        self.freq[number] += 1
        self.freq_cnter[self.freq[number]] += 1

    def deleteOne(self, number: int) -> None:
        if 0 == self.freq[number]:
            return
        self.freq_cnter[self.freq[number]] -= 1
        self.freq[number] -= 1
        self.freq_cnter[self.freq[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return 0 < self.freq_cnter[frequency]
