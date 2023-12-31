def main() -> None:
    nums = []
    for _ in range(6):
        nums += map(int, input().split())

    ans = 0, 0
    for num in nums:
        cnt = 0
        for i in range(num, 0, -1):
            if 0 == num % i:
                cnt += 1
        if cnt > ans[0]:
            ans = cnt, num
    print(ans)


if __name__ == '__main__':
    main()

'''
393353 901440 123481 850930 423154 240461
373746 232926 396677 486579 744860 468782
941389 777714 992588 343292 385198 876426
483857 241899 544851 647930 772403 109929
882745 372491 877710 340000 659788 658675
296521 491295 609764 718967 842000 670302
'''
