def getsum(num) -> int:
    res = 0
    for ch in num:
        res = res + int(ch)
    return res


def main() -> None:
    nums = [input().split() for _i in range(8)]
    print(nums)
    min_ = 54
    for i in range(8):
        for j in range(8):
            newsum = getsum(nums[i][j])
            if newsum < min_:
                min_ = newsum
                ans = nums[i][j]
            if newsum == min_:
                print(nums[i][j])
    print(ans)


if __name__ == '__main__':
    main()

'''
454771 329157 801601 580793 755604 931703 529875 361797
604358 529564 574776 821517 195563 688516 223321 607845
284772 603562 543328 707484 533688 380468 233733 257995
896582 670074 912386 702393 722092 834842 126346 606526
376981 910643 413754 945725 817853 651778 350775 676550
316935 487808 939526 900568 423326 298936 927671 539773
136326 717022 886675 466684 436470 558644 267231 902422
743580 857864 529622 320921 595409 486860 951114 558787
'''
