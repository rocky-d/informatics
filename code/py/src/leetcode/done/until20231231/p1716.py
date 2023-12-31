class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        whole_weeks, days_left = n // 7, n % 7
        one_week = 28
        for i in range(whole_weeks):
            ans += one_week
            one_week += 7
        one_day = 1 + whole_weeks
        for i in range(days_left):
            ans += one_day
            one_day += 1
        return ans
