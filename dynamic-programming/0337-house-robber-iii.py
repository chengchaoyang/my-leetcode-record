"""
在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。
除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。
如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

示例 1:

输入: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

输出: 7
解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
示例 2:

输入: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \
 1   3   1

输出: 9
解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        sum = 0
        if root is None:
            return sum
        sum1 = 0
        sum2 = 0
        sum1 += self.rob(root.left) + self.rob(root.right)
        if root.left and root.right:
            sum2 += root.val + self.rob(root.left.left) + self.rob(root.right.right)
        elif root.left and not root.right:
            sum2 += root.val + self.rob(root.left.left)
        elif not root.left and  root.right:
            sum2 += root.val + self.rob(root.right.right)
        else:
            sum2 += root.val
        return max(sum1,sum2)



class Solution:
    def rob(self, root: TreeNode) -> int:
        #
        def robinteger(root):
            # 如果节点本身就是空的，那无论偷不偷，都拿不到钱
            res = [0, 0]
            if not root: return res
            # res[1]表示节点被偷能拿到的最多的钱
            # 节点被偷的话，其子节点不能被偷
            left = robinteger(root.left)
            right = robinteger(root.right)
            res[1] += root.val + left[0] + right[0]
            # res[0]表示不偷该节点能拿到的最多的钱
            # 不被偷的话，无论其子节点是否被偷都可以
            res[0] += max(left[0], left[1]) + max(right[0], right[1])
            return res

        res = robinteger(root)
        return max(res[0], res[1])