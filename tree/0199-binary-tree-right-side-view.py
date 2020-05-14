"""
给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例:

输入: [1,2,3,null,5,null,4]
输出: [1, 3, 4]
解释:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-right-side-view
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
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
    BFS
    """
    def rightSideView(self, root: TreeNode) -> List[int]:
        result = []
        if root is None:
            return result
        queue = [root]
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(node.val)
        return result

class Solution:
    """
    DFS
    """
    def rightSideView(self, root: TreeNode) -> List[int]:
        def dfs(node, res, depth):
            if node is None:
                return
            if len(res) == depth:
                res.append(node.val)
            dfs(node.right, res, depth + 1)
            dfs(node.left, res, depth + 1)

        res = []
        dfs(root, res, 0)
        return res

