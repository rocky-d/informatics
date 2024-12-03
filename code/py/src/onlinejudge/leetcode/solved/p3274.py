class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        return 0b0 == 0b1 & abs(ord(coordinate1[0]) - ord(coordinate2[0])) + abs(int(coordinate1[1]) - int(coordinate2[1]))
