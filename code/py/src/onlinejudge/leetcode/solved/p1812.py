class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return 0b1 == 0b1 & (ord(coordinates[0]) ^ ord(coordinates[1]))
