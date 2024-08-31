class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        loss = numExchange - 1
        return numBottles // loss + (numBottles if 0 < numBottles % loss else numBottles - 1)
