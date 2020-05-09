"""
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List
from collections import defaultdict
class Solution:
    """
    迭代解法,复杂度太高
    """
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        res = defaultdict(list)
        if root is None:
            return result
        queue = [(0,root)]
        while queue:
            level,node = queue.pop(0)
            res[level].append(node.val)
            level+=1
            if node.left:
                queue.append((level,node.left))
            if node.right:
                queue.append((level,node.right))

        for i in range(len(res)):
            result.append(res[i])
        return result


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if root is None:
            return res
        queue = [root]
        res = []
        while queue:
            size = len(queue)
            cur = []
            for _ in range(size):
                top = queue.pop(0)
                cur.append(top.val)
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
            res.append(cur)
        return res