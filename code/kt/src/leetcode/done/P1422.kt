package leetcode.done

import kotlin.math.max

class P1422 {
    fun maxScore(s: String): Int {
        val cnt0: IntArray = IntArray(s.length)
        for (p in 0 until s.lastIndex) {
            cnt0[p + 1] = cnt0[p] + if ('0' == s[p]) 1 else 0
        }
        val cnt1: IntArray = IntArray(s.length)
        for (p in s.lastIndex downTo 1) {
            cnt1[p - 1] = cnt1[p] + if ('1' == s[p]) 1 else 0
        }
        var ans: Int = 0
        for (p in 0 until s.lastIndex) {
            ans = max(ans, cnt0[p + 1] + cnt1[p])
        }
        return ans
    }
}