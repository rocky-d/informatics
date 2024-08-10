def main() -> None:
    n = int(input())
    s = input()

    dp = {'R': 0, 'P': 0, 'S': 0}
    for c in s:
        if 'R' == c:
            dp['R'], dp['P'] = max(dp['P'], dp['S']), max(dp['R'], dp['S']) + 1
        elif 'P' == c:
            dp['P'], dp['S'] = max(dp['R'], dp['S']), max(dp['R'], dp['P']) + 1
        else:  # elif 'S' == c:
            dp['S'], dp['R'] = max(dp['R'], dp['P']), max(dp['P'], dp['S']) + 1
    print(max(dp.values()))


if __name__ == '__main__':
    main()
