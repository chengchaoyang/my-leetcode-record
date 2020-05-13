"""
给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定的有序链表： [-10, -3, 0, 5, 9],

一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    重点是找到链表的中点
    """
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head is None:
            return None
        if head.next is None:
            return TreeNode(head.val)
        fast = head
        slow = head
        pre = None
        while fast.next and fast.next.next:
            fast = fast.next.next
            pre = slow
            slow = slow.next
        root = TreeNode(slow.val)
        right = slow.next
        slow.next = None
        # 当链表只有 2 个结点的时候，pre 指针此时为 None，不用递归构造左子树
        if pre:
            pre.next = None
            root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(right)
        return root

