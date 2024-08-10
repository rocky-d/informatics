package onlinejudge.leetcode.solved

class P1 {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        val map = HashMap<Int, Int>(nums.size)
        nums.forEachIndexed { index, number ->
            val other = target - number
            map[other]?.let {
                return intArrayOf(it, index)
            }
            map[number] = index
        }
        return intArrayOf()
    }
}
