package leetcode.done

class P326 {
    fun isPowerOfThree(n: Int): Boolean {
        if (1 > n) {
            return false
        }
        var varN: Int = n
        while (0 == varN % 3) {
            varN /= 3
        }
        return 1 == varN
    }
}