def main():
    words = set()
    with open(r'./LQSP2025_PB/words.txt', 'r') as f:
        for line in f.readlines():
            words.add(line.strip('\n'))
    words = sorted(words, key=lambda word: (len(word), word))
    beauties = {'': ''}
    for word in words:
        if ''.join(sorted(word[:-1])) not in beauties:
            continue
        key = ''.join(sorted(word))
        beauties[key] = min(beauties.get(key, word), word)
    print(min(beauties.values(), key=lambda word: (-len(word), word)))


main()
# afplcu
