"""
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为
一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]


示例 1:
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
示例 2:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
 

说明:

所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉树中。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    1) 对于root节点: 如果root为空节点,返回null
　　　　如果root与p或q相等,返回p或q.

　　2) 如果没有在情况1返回,说明root不为空并且不与p,q相等
　　　　那么,可能节点的分布存在以下情况:
　　　　一:节点一个分布在root的左子树一个分布在root的右子树
　　　　二:节点都分布在root的左子树
　　　　三:节点都分布在root的右子树

　　　　我们对左右节点分别进行递归.左右节点分别成为新root节点.(记为新root节点)
　　　　　　　　
　　3) 那么,左右两个搜索方法的返回值 searchLeft和searchRight 也根据搜索有了不同的情况
　　　　一: searchLeft 和 searchRight 都不为空,对应着情况一
　　　　二: searchLeft不为空,searchRight为空 , 对应着情况二
　　　　三: searchRight不为空,searchLeft为空 , 对应着情况三
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if left != None and right != None:
            return root
        if left is None:
            return right
        else:
            return left