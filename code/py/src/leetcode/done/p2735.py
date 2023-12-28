from rockyutil.leetcode import *


class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        costs, max_move_cost = [], 0
        for i in range(n):
            costs.append(0)
            cost, move_cost = 1_000_000_000 + n * x, 0
            for j in range(i, n):
                if cost > nums[j] + move_cost:
                    cost = nums[j] + move_cost
                    costs[-1], max_move_cost = nums[j], max(max_move_cost, move_cost)
                move_cost += x
                if cost <= move_cost:
                    break
            else:
                for j in range(0, i):
                    if cost > nums[j] + move_cost:
                        cost = nums[j] + move_cost
                        costs[-1], max_move_cost = nums[j], max(max_move_cost, move_cost)
                    move_cost += x
                    if cost <= move_cost:
                        break
        return max_move_cost + sum(costs)
