# 1 + 2*1 + 3*2*1 + 4*3*2*1 + 5*4*3*2*1 + 6*5*4*3*2*1
# 1 + 1 * (2 + 3*2 + 4*3*2 + 5*4*3*2 + 6*5*4*3*2)
# 1 + 1 * (2 + 2 * (3 + 4*3 + 5*4*3 + 6*5*4*3))
# 1 + 1 * (2 + 2 * (3 + 3 * (4 + 5*4 + 6*5*4)))
# 1 + 1 * (2 + 2 * (3 + 3 * (4 + 4 * (5 + 6 * 5))))
# 1 + 1 * (2 + 2 * (3 + 3 * (4 + 4 * (5 + 5 * (6)))))

def main():
    s = int(input())
    res = s
    for i in range(s - 1, 0, -1):
        res = i + i * res
    print(res)


if __name__ == '__main__':
    main()