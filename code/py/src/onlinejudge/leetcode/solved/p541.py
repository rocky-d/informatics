class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        return ''.join(s[i : i + k] if 0b1 == 0b1 & i // k else s[i : i + k][::-1] for i in range(0, len(s), k))
