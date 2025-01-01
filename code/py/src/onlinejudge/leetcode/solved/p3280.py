class Solution:
    def convertDateToBinary(self, date: str) -> str:
        return '-'.join(bin(int(item))[2:] for item in date.split('-'))
