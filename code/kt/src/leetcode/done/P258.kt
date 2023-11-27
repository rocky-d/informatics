package leetcode.done

class P258 {
    fun addDigits(num: Int): Int {
        return if (0 == num) 0 else if (0 == num % 9) 9 else num % 9
    }
}