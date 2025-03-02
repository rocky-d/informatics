from onlinejudge.leetcode import *


class ATM:
    def __init__(self) -> None:
        self.banknotes = [0] * 5

    def deposit(self, banknotesCount: List[int]) -> None:
        for idx, cnt in enumerate(banknotesCount):
            self.banknotes[idx] += cnt

    def withdraw(self, amount: int) -> List[int]:
        res = [0] * 5
        for idx, denomination in zip((4, 3, 2, 1, 0), (500, 200, 100, 50, 20)):
            res[idx] = min(self.banknotes[idx], amount // denomination)
            amount -= denomination * res[idx]
            if 0 == amount:
                break
        else:
            return [-1]
        for idx, cnt in enumerate(res):
            self.banknotes[idx] -= cnt
        return res
