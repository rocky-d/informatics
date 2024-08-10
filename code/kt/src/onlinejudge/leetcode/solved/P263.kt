package onlinejudge.leetcode.solved

class P263 {
    fun isUgly(n: Int): Boolean {
        if (1 > n) {
            return false
        }
        var varN: Int = n
        for (i in intArrayOf(2, 3, 5)) {
            while (0 == varN % i) {
                varN /= i
            }
        }
        return 1 == varN
    }
}
