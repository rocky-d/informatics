package onlinejudge.leetcode.solved

import kotlin.math.max

class P1422 {
    fun maxScore(s: String): Int {
        val leftZeros: IntArray = IntArray(s.length)
        for (p in 0 until s.lastIndex) {
            leftZeros[p + 1] = leftZeros[p] + if ('0' == s[p]) 1 else 0
        }
        val rightOnes: IntArray = IntArray(s.length)
        for (p in s.lastIndex downTo 1) {
            rightOnes[p - 1] = rightOnes[p] + if ('1' == s[p]) 1 else 0
        }
        var ans: Int = 0
        for (p in 0 until s.lastIndex) {
            ans = max(ans, leftZeros[p + 1] + rightOnes[p])
        }
        return ans
    }
}