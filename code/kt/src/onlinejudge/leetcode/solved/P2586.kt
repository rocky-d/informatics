package onlinejudge.leetcode.solved

class P2586 {
    fun vowelStrings(words: Array<String>, left: Int, right: Int): Int {
        var ans: Int = 0
        for (word in words.slice(left..right)) {
            if ((word.startsWith('a') || word.startsWith('e') || word.startsWith('i') || word.startsWith('o') || word.startsWith('u')) && (word.endsWith('a') || word.endsWith('e') || word.endsWith('i') || word.endsWith('o') || word.endsWith('u'))) {
                ++ans
            }
        }
        return ans
    }
}
