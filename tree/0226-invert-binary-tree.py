"""
翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1
备注:
这个问题是受到 Max Howell 的 原问题 启发的 ：

谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/invert-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        left = self.invertTree(root.right)
        right = self.invertTree(root.left)
        root.left = left
        root.right = right
        return root


class Solution:

    # 中序遍历,左->根->右

    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return
        self.invertTree(root.left)

        # 交换左右子树
        root.left, root.right = root.right, root.left

        # 注意：这里的 root.left 就是交换之前的 root.right
        self.invertTree(root.left)
        return root


class Solution:

    # 前序遍历

    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return

        # 交换左右子树
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

class Solution:

    # 后序遍历

    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return

        self.invertTree(root.left)
        self.invertTree(root.right)

        # 交换左右子树
        root.left, root.right = root.right, root.left
        return root


class Solution:

    # 层序遍历，用一个队列记录原始的需要遍历的节点顺序。

    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None

        queue = [root]

        while queue:
            cur_node = queue.pop(0)

            if cur_node.left or cur_node.right:
                cur_node.left, cur_node.right = cur_node.right, cur_node.left

                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)

        return root