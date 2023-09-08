class Solution:
    def __init__(self) -> None:
        self.res = 0
        self.words = {input().strip(): 2 for _ in range(int(input()))}
        start = input().strip()

        for word in self.words.keys():
            if word.startswith(start):
                self.words[word] -= 1
                self.dfs(word, len(word))
                self.words[word] += 1
        print(self.res)

    def dfs(self, pre_word: str, cnt: int) -> None:
        self.res = max(self.res, cnt)
        for word in self.words.keys():
            if self.words[word] > 0:
                for i in range(1, len(pre_word)):
                    if word.startswith(pre_word[i:]):
                        self.words[word] -= 1
                        self.dfs(word, cnt + len(word) - len(pre_word) + i)
                        self.words[word] += 1


if __name__ == '__main__':
    Solution()
