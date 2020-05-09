"""
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#中序遍历，左->根->右
#################递归#################################
from typing import List
class Solution:
    def __init__(self):
        self.result = []
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return self.result
        self.inorderTraversal(root.left)
        self.result.append(root.val)
        self.inorderTraversal(root.right)
        return self.result

#################迭代#################################
class Solution:

    # “模拟系统栈”实现的二叉树“中序遍历”（推荐）

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = [(1, root)]
        while stack:
            command, node = stack.pop()
            if not node:
                continue
            if command == 0:
                res.append(node.val)
            if command == 1:
                # 左，自己，右，反过来就是
                # 右边，自己，左边
                stack.append((1, node.right))
                stack.append((0, node))
                stack.append((1, node.left))
        return res


class Solution:

    # “模拟系统栈”实现的二叉树“中序遍历”（推荐）

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        # 1 表示递归处理
        stack = [(1, root)]
        res = []
        while stack:
            command, node = stack.pop()
            if command == 0:
                # 0 表示当前马上执行将结点的值添加到结果集中
                res.append(node.val)
            else:
                # 关键在这里：因为是模拟系统栈，应该把中序遍历的顺序倒过来写
                # 调整一下顺序就可以完成前序遍历和后序遍历
                if node.right:
                    stack.append((1, node.right))
                stack.append((0, node))
                if node.left:
                    stack.append((1, node.left))
        return res