"""
给定一个二叉树，返回所有从根节点到叶子节点的路径。
说明: 叶子节点是指没有子节点的节点。

示例:
输入:

   1
 /   \
2     3
 \
  5

输出: ["1->2->5", "1->3"]

解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-paths
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
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        if root is None:
            return res
        self.__dfs(root,res,[])
        return res

    def __dfs(self,root,res,path):
        if root is None:
            return
        path.append(str(root.val))
        if root.left is None and root.right is None:
            res.append("->".join(path[:]))
        if root.left:
            self.__dfs(root.left,res,path)
        if root.right:
            self.__dfs(root.right,res,path)
        path.pop()


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        if root is None:
            return res
        self.__helper(root, [str(root.val)], res)
        return res

    def __helper(self, node, pre, res):
        # 隐式回溯
        # pre 表示一组解
        if node is None:
            return
        if node.left is None and node.right is None:
            res.append('->'.join(pre))
        # 通过参数传递的方式，就没有显式的回溯和状态重置的过程了
        if node.left:
            self.__helper(node.left, pre + [str(node.left.val)], res)
        if node.right:
            self.__helper(node.right, pre + [str(node.right.val)], res)