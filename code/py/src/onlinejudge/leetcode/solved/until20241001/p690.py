from onlinejudge.leetcode import *


# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List[Employee], id: int) -> int:
        employees_dct = {}
        for employee in employees:
            employees_dct[employee.id] = employee
        employees = employees_dct

        def dfs(id: int) -> int:
            employee = employees[id]
            return employee.importance + sum(dfs(subordinate) for subordinate in employee.subordinates)

        return dfs(id=id)
