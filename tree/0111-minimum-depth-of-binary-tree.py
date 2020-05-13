"""
给定一个二叉树，找出其最小深度。
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.
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
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None:
            return self.minDepth(root.right)+1
        if root.right is None:
            return self.minDepth(root.left)+1
        return min(self.minDepth(root.left),self.minDepth(root.right))+1


class Solution:
    "BFS"
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        depth = 0
        queue = [root]
        while queue:
            depth += 1
            size = len(queue)
            for _ in range(size):
                first = queue.pop(0)
                if first.left is None and first.right is None:
                    return depth
                if first.left:
                    queue.append(first.left)
                if first.right:
                    queue.append(first.right)