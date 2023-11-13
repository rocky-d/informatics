package leetcode.done

import rockyutil.TreeNode

class P2236 {
    fun checkTree(root: TreeNode?): Boolean {
        return root!!.`val` == root.left!!.`val` + root.right!!.`val`
    }
}