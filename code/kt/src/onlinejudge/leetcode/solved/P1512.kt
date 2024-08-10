package onlinejudge.leetcode.solved

class P1512 {
    fun numIdenticalPairs(nums: IntArray): Int {
        var ans: Int = 0
        val notVed: BooleanArray = BooleanArray(nums.size) { true }
        for (i in 0..nums.lastIndex) {
            if (notVed[i]) {
                var cnt: Int = 1
                for (j in i + 1..nums.lastIndex) {
                    if (nums[i] == nums[j]) {
                        notVed[j] = false
                        ++cnt
                    }
                }
                ans += cnt * (cnt - 1) / 2
            }
        }
        return ans
    }
}

//fun main() {
//    val sol: P1512 = P1512()
//
//    val egNums: IntArray = intArrayOf(1, 2, 3, 1, 1, 3)
//    println(sol.numIdenticalPairs(nums = egNums))
//}