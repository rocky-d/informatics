package onlinejudge.leetcode.solved

class P1486 {
    fun xorOperation(n: Int, start: Int): Int {
        val nums = Array(n) { i -> start + 2 * i }
        var ans = 0
        for (num in nums) {
            ans = ans xor num
        }
        return ans
    }
}
