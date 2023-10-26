package leetcode.done

class P2469 {
    fun convertTemperature(celsius: Double): DoubleArray {
        val ans = DoubleArray(2)
        ans[0] = celsius + 273.15
        ans[1] = celsius * 1.80 + 32.00
        return ans
    }
}