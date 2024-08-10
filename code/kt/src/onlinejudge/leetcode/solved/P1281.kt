package onlinejudge.leetcode.solved

class P1281 {
    fun subtractProductAndSum(n: Int): Int {
        var varN: Int = n
        var num1: Int = 1
        var num2: Int = 0
        while (varN > 0) {
            val digit = varN % 10
            num1 *= digit
            num2 += digit
            varN /= 10
        }
        return num1 - num2
    }
}