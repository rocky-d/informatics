package onlinejudge.leetcode.solved

import kotlin.math.abs

class P1534 {
    fun countGoodTriplets(arr: IntArray, a: Int, b: Int, c: Int): Int {
        var ans: Int = 0
        for (i in 0..arr.lastIndex) {
            for (j in i + 1..arr.lastIndex) {
                for (k in j + 1..arr.lastIndex) {
                    if (abs(arr[i] - arr[j]) <= a && abs(arr[j] - arr[k]) <= b && abs(arr[i] - arr[k]) <= c) {
                        ++ans
                    }
                }
            }
        }
        return ans
    }
}