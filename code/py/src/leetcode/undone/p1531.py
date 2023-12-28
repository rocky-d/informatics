class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        len_s = len(s)
        len_encoded_s, encoded_s_list = 0, []
        pointer = 0
        while pointer < len_s:
            char = s[pointer]
            times = 1
            pointer += 1
            while pointer < len_s and char == s[pointer]:
                times += 1
                pointer += 1
            len_encoded_s += 1 + len('' if 1 == times else str(times))
            encoded_s_list.append((char, times))
        print(encoded_s_list)

        dp = [0 for _ in range(1 + k)]
        for i, item in enumerate(encoded_s_list):
            if 1 <= i <= len(encoded_s_list) - 2 and encoded_s_list[i - 1][0] == encoded_s_list[i + 1][0]:
                left, right = encoded_s_list[i - 1][1], encoded_s_list[i + 1][1]
                extra = 1 + len('' if 1 == left else str(left)) + len('' if 1 == right else str(right)) - len(
                    str(encoded_s_list[i - 1][1] + encoded_s_list[i + 1][1]))
            else:
                extra = 0
            for j in range(k, 0, -1):
                if 1 == item[1]:
                    cost = 1
                    dp[j] = max(dp[j], dp[j - cost] + 1 + extra)
                else:
                    for cost in range(1, 1 + min(item[1] - 2, j)):
                        dp[j] = max(dp[j], dp[j - cost] + len(str(item[1])) - len(str(item[1] - cost)))
                    cost = item[1] - 1
                    if cost <= j:
                        dp[j] = max(dp[j], dp[j - cost] + len(str(item[1])))
                        cost = item[1]
                        if cost <= j:
                            dp[j] = max(dp[j], dp[j - cost] + 1 + len(str(item[1])) + extra)
            print(dp)
        return len_encoded_s - dp[-1]


# a2ba2b2cb3ac3
eg_s = 'aabaabbcbbbaccc'
eg_k = 6
print(Solution().getLengthOfOptimalCompression(s = eg_s, k = eg_k))
