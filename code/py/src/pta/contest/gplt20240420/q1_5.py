def main():
    n = int(input())
    words = [input() for _ in range(n)]
    k = int(input())
    target = input()
    target_len = len(target)
    sub = '<censored>'

    subt = []
    avail = [True] * target_len
    for word in words:
        word_len = len(word)
        idx, length = 0, len(target)
        while idx < length:
            if target[idx:idx + word_len] == word and all(avail[idx:idx + word_len]):
                for j in range(idx, min(idx + word_len, target_len)):
                    avail[j] = False
                subt.append((idx, word_len))
                idx += word_len
            else:
                idx += 1
    cnt = len(subt)
    if cnt < k:
        subt.sort(key = lambda item: -item[0])
        for i, word_len in subt:
            target = target[:i] + sub + target[i + word_len:]
        print(target)
    else:
        print(cnt)
        print('He Xie Ni Quan Jia!')


if __name__ == '__main__':
    main()
