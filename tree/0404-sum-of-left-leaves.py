"""
计算给定二叉树的所有左叶子之和。

示例：

    3
   / \
  9  20
    /  \
   15   7

在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-of-left-leaves
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # 关键在于判断是否是左边叶子结点
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0
        # 1、左边非空
        # 2、左边的左边是空
        # 3、左边的右边是空
        if root.left is not None and root.left.left is None and root.left.right is None:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)


class Solution:
    # BFS
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0

        queue = [root]
        res = 0
        while queue:
            top = queue.pop(0)
            if top.left and top.left.left is None is top.left.right is None:
                res += top.left.val
            if top.left:
                queue.append(top.left)
            if top.right:
                queue.append(top.right)
        return res