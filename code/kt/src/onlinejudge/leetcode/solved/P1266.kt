package onlinejudge.leetcode.solved

import kotlin.math.abs
import kotlin.math.min

class P1266 {
    fun minTimeToVisitAllPoints(points: Array<IntArray>): Int {
        var ans: Int = 0
        var x: Int = points[0][0]
        var y: Int = points[0][1]
        for (point in points.slice(1..points.lastIndex)) {
            val stepX: Int = abs(x - point[0])
            val stepY: Int = abs(y - point[1])
            ans += stepX + stepY - min(stepX, stepY)
            x = point[0]
            y = point[1]
        }
        return ans
    }
}