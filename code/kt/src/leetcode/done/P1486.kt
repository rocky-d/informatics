package leetcode.done

class P1486 {
    fun xorOperation(n: Int, start: Int): Int {
        val nums = Array(n) { index -> start + 2 * index }
        var ans = 0
        for (num in nums) {
            ans = ans xor num
        }
        return ans
    }
}