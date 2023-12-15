from rockyutil.leetcode import *


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        froms, tos = set(), set()
        for city_a, city_b in paths:
            froms.add(city_a)
            tos.add(city_b)
        return tuple(tos - froms)[0]
