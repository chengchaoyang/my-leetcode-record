"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/validate-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        lower = float("-inf")
        upper = float("inf")
        return self.__helper(root,lower,upper)

    def __helper(self,root,lower,upper):
        if root is None:
            return True
        if self.__helper(root.left,lower,root.val) and self.__helper(root.right,root.val,upper):
            if lower < root.val and root.val < upper:
                return True
        return False

class Solution(object):
    def isValidBST(self, root, left=None, right=None):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if left and left.val >= root.val:
            return False
        if right and right.val <= root.val:
            return False
        return self.isValidBST(root.left, left, root) and self.isValidBST(root.right, root, right)