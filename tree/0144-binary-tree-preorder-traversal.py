"""

给定一个二叉树，返回它的 前序 遍历。

 示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,2,3]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List

class Solution:
    """
    递归解法
    """
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.__dfs(root,res)
        return res

    def __dfs(self,root,res):
        if root is None:
            return
        res.append(root.val)
        self.__dfs(root.left,res)
        self.__dfs(root.right,res)


class Solution:
    """
    迭代解法
    """
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if root is None:
            return res
        stack = [(1,root)]
        while stack:
            command, node = stack.pop()
            if command == 0:
                res.append(node.val)
            else:
                if node.right:
                    stack.append((1,node.right))
                if node.left:
                    stack.append((1,node.left))
                stack.append((0,node))
        return res