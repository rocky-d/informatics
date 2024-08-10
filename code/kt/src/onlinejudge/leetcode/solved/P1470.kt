package leetcode.done

class P1470 {
    fun shuffle(nums: IntArray, n: Int): IntArray {
        return IntArray(2 * n) { i: Int -> if (0 == i % 2) nums[i / 2] else nums[n + i / 2] }
    }
}