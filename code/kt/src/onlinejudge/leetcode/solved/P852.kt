package onlinejudge.leetcode.solved

class P852 {
    fun peakIndexInMountainArray(arr: IntArray): Int {
        val n: Int = arr.size
        var left: Int = 1
        var right: Int = n - 2
        while (left <= right) {
            val middle: Int = (left + right) / 2
            if (arr[middle] > arr[middle + 1]) {
                right = middle - 1
            } else {
                left = middle + 1
            }
        }
        return left
    }
}