package onlinejudge.leetcode.solved

class P2413 {
    fun smallestEvenMultiple(n: Int): Int {
        return if (0 == n % 2) n else 2 * n
    }
}