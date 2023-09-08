def dfs(words:dict, pre_word: str, cnt: int) -> None:
    print(pre_word)
    for word in words.keys():
        if words[word] > 0:
            for i in range(1, len(pre_word)):
                if word.startswith(pre_word[i:]):
                    words[word] -= 1
                    dfs(words, word)
                    words[word] += 1

def main() -> None:
    words = {input(): 2 for _ in range(int(input()))}
    start = input()
    print(words)
    print(start)

    cnt = 0
    res = 0

    for word in words.keys():
        if word.startswith(start):
            words[word] -= 1
            cnt +=
            dfs(words, word, cnt)
            words[word] += 1




if __name__ == '__main__':
    main()
