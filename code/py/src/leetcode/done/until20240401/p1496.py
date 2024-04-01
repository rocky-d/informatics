class Solution:
    def isPathCrossing(self, path: str) -> bool:
        seen = set()
        point = 0, 0
        seen.add(point)
        for step in path:
            match step:
                case 'N':
                    point = point[0], point[1] + 1
                case 'S':
                    point = point[0], point[1] - 1
                case 'E':
                    point = point[0] + 1, point[1]
                case 'W':
                    point = point[0] - 1, point[1]
            if point in seen:
                ans = True
                break
            else:
                seen.add(point)
        else:
            ans = False
        return ans
