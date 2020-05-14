"""
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
说明: 叶子节点是指没有子节点的节点。
示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:
[
   [5,4,11,2],
   [5,8,4,5]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum-ii
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
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        self.__dfs([], root, sum, res)
        return res

    def __dfs(self,path,root,sum,results):
        if root is None:
            return
        if root.left is None and root.right is None and root.val==sum:
            result = []
            result.extend(path)
            result.append(root.val)
            results.append(result)
            return
        path.append(root.val)
        if root.left:
            self.__dfs(path, root.left, sum - root.val, results)
        if root.right:
            self.__dfs(path, root.right, sum - root.val, results)
        #这一步很关键
        path.pop()


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        if root is None:
            return res
        self.__dfs(root, [], sum, res)
        return res

    def __dfs(self, node, path, sum, res):
        # 递归，就应该先写递归终止条件
        if node is None:
            return
        # 走到这里 node 肯定非空，所以可以使用 left 和 right 成员变量
        # 走完以后，要记得回溯，状态要重置
        # 先把它加到路径中，在各种 if 都不成立的最后，要记得 pop 出去
        path.append(node.val)
        if node.left is None and node.right is None:
            # 如果是叶子结点，并且 residue 就等于当前结点的值
            if node.val == sum:
                res.append(path[:])
                # 注意：这里不要 return ，如果要 return，return 之前把 path 执行 pop 操作
        # 走到这里是非叶子结点，所以左边要走一走，右边也要走一走
        if node.left:
            self.__dfs(node.left, sum - node.val, path, res)
        if node.right:
            self.__dfs(node.right, sum - node.val, path, res)
        path.pop()
