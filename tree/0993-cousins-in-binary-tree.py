"""
在二叉树中，根节点位于深度 0 处，每个深度为 k 的节点的子节点位于深度 k+1 处。
如果二叉树的两个节点深度相同，但父节点不同，则它们是一对堂兄弟节点。
我们给出了具有唯一值的二叉树的根节点 root，以及树中两个不同节点的值 x 和 y。
只有与值 x 和 y 对应的节点是堂兄弟节点时，才返回 true。否则，返回 false。

示例 1：
输入：root = [1,2,3,4], x = 4, y = 3
输出：false

示例 2：
输入：root = [1,2,3,null,4,null,5], x = 5, y = 4
输出：true

示例 3：
输入：root = [1,2,3,null,4], x = 2, y = 3
输出：false
 
提示：
二叉树的节点数介于 2 到 100 之间。
每个节点的值都是唯一的、范围为 1 到 100 的整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cousins-in-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    "BFS"
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root is None:
            return False
        queue = [root]
        while queue:
            size = len(queue)
            x_index = None
            y_index = None
            for i in range(size):
                node = queue.pop(0)
                if node:
                    if node.val == x:
                        x_index  = i
                    if node.val == y:
                        y_index = i
                    queue.append(node.left)
                    queue.append(node.right)
                if x_index is not None and y_index is not None:
                    if abs(x_index-y_index) > 1:
                        return True
                    if abs(x_index-y_index) == 1:
                        if x_index > y_index and x_index % 2 == 0:
                            return True
                        if x_index < y_index and y_index % 2 == 0:
                            return True
        return False


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(4)
root.right = TreeNode(5)
root.right.right = TreeNode(6)
print(Solution().isCousins(root,3,6))