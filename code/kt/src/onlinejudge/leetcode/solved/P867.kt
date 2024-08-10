package onlinejudge.leetcode.solved

class P867 {
    fun transpose(matrix: Array<IntArray>): Array<IntArray> {
        val ans: Array<IntArray> = Array(matrix[0].size) { IntArray(matrix.size) }
        for (i in matrix.indices) {
            for (j in matrix[i].indices) {
                ans[j][i] = matrix[i][j]
            }
        }
        return ans
    }
}
