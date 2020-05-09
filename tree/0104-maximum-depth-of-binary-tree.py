"""
给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-depth-of-binary-tree
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
    """
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1


class Solution:
    """
    层序遍历
    """
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        level = 1
        queue = [(level,root)]
        while queue:
            size = len(queue)
            for _ in range(size):
                level,node = queue.pop(0)
                if node.left:
                    queue.append((level+1,node.left))
                if node.right:
                    queue.append((level+1,node.right))
        return level

class Solution:
    """
    层序遍历，BFS
    """
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        depth = 0
        queue = [root]
        while queue:
            size = len(queue)
            depth += 1
            for _ in range(size):
                first = queue.pop(0)
                if first.left:
                    queue.append(first.left)
                if first.right:
                    queue.append(first.right)
        return depth

