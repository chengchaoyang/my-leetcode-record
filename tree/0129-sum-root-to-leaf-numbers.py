"""
给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。
例如，从根到叶子节点路径 1->2->3 代表数字 123。
计算从根到叶子节点生成的所有数字之和。

说明: 叶子节点是指没有子节点的节点。

示例 1:

输入: [1,2,3]
    1
   / \
  2   3
输出: 25
解释:
从根到叶子节点路径 1->2 代表数字 12.
从根到叶子节点路径 1->3 代表数字 13.
因此，数字总和 = 12 + 13 = 25.
示例 2:

输入: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
输出: 1026
解释:
从根到叶子节点路径 4->9->5 代表数字 495.
从根到叶子节点路径 4->9->1 代表数字 491.
从根到叶子节点路径 4->0 代表数字 40.
因此，数字总和 = 495 + 491 + 40 = 1026.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-root-to-leaf-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        sum = 0
        if root is None:
            return sum
        res = []
        self.__dfs(root,[],res)
        for path in res:
            path_s = ''
            for i in path:
                path_s += str(i)
            sum += int(path_s)
        return sum


    def __dfs(self,root,path,res):
        if root is None:
            return
        path.append(root.val)
        if root.left is None and root.right is None:
            res.append(path[:])
        if root.left:
            self.__dfs(root.left,path,res)
        if root.right:
            self.__dfs(root.right,path,res)
        path.pop()


class Solution:

    def __init__(self):
        self.res = 0

    def sumNumbers(self, root: TreeNode) -> int:

        if root is None:
            return 0
        if root.left:
            # 如果左边非空
            root.left.val += root.val * 10
        if root.right:
            # 如果右边非空
            root.right.val += root.val * 10
        # 如果左边右边都为空，就可以结算了
        if root.left is None and root.right is None:
            self.res += root.val
        # 前序遍历
        self.sumNumbers(root.left)
        self.sumNumbers(root.right)
        return self.res

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        res = []
        self.__dfs(root, 0, res)
        return sum(res)

    # Python 中对于基础的数据类型是值传递，即复制
    def __dfs(self, root, cum_sum, res):
        if root is None:
            return None
        if root.left is None and root.right is None:
            # 结算
            res.append(cum_sum * 10 + root.val)
            return
        self.__dfs(root.left, cum_sum * 10 + root.val, res)
        self.__dfs(root.right, cum_sum * 10 + root.val, res)