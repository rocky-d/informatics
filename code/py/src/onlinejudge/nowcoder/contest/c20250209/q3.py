from collections import Counter, defaultdict


def main() -> None:
    nums1 = map(int, input().split(','))
    nums2 = map(int, input().split(','))

    cnter1 = Counter(nums1)
    cnter2 = Counter(nums2)
    cnter = Counter()
    for num in cnter1.keys() & cnter2.keys():
        cnter[num] = min(cnter1[num], cnter2[num])
    if 0 == len(cnter):
        print('NULL')
        return
    dct = defaultdict(lambda: [])
    for num, cnt in cnter.items():
        dct[cnt].append(num)
    for cnt in sorted(dct.keys()):
        print(f"{cnt}:{','.join(map(str, sorted(dct[cnt])))}")


main()
