package onlinejudge.leetcode.solved

import kotlin.math.min

class P1423 {
    fun maxScore(cardPoints: IntArray, k: Int): Int {
        val n: Int = cardPoints.size
        val l: Int = n - k
        val prefixSum: IntArray = IntArray(1 + n)
        for (i in cardPoints.indices) {
            prefixSum[i + 1] = prefixSum[i] + cardPoints[i]
        }
        return if (0 == l) {
            prefixSum[n]
        } else {
            var minWindow: Int = prefixSum[n]
            for (i in 0..k) {
                minWindow = min(minWindow, prefixSum[i + l] - prefixSum[i])
            }
            prefixSum[n] - minWindow
        }
    }
}
