"""
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
 
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
 
进阶：

你可以运用递归和迭代两种方法解决这个问题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/symmetric-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    递归解法
    还可以使用队列去完成
    https://leetcode.com/problems/symmetric-tree/solution/
    """
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.__helper(root.left, root.right)

    def __helper(self, left_node, right_node):
        if left_node is None and right_node is None:
            return True
        if left_node is None or right_node is None or left_node.val != right_node.val:
            return False
        return self.__helper(left_node.left, right_node.right) and self.__helper(
            left_node.right, right_node.left)


class Solution:
    """
    迭代解法
    用队列去完成
    https://leetcode.com/problems/symmetric-tree/solution/
    """
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        queue = [root]
        while queue:
            size = len(queue)
            cur = []
            for _ in range(size):
                node = queue.pop(0)
                if node:
                    cur.append(node.val)
                else:
                    cur.append(None)
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
            l = 0
            r = len(cur) - 1
            while l < r:
                if cur[l] != cur[r]:
                    return False
                l += 1
                r -= 1
        return True


