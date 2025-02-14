from onlinejudge.leetcode import *


class ProductOfNumbers:
    def __init__(self) -> None:
        self.prefs = [1]

    def add(self, num: int) -> None:
        self.prefs.append(self.prefs[-1] * num)

    def getProduct(self, k: int) -> int:
        return self.prefs[-1] // self.prefs[-1 - k]
