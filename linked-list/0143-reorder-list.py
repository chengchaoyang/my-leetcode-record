"""
给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例 1:
给定链表 1->2->3->4, 重新排列为 1->4->2->3.

示例 2:
给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reorder-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    """
    自己写出来的
    1.先找到中点
    2.对中点以后的节点做翻转
    3.合并两个链表
    """
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None:
            return head
        dummy_head = ListNode(-1)
        slow = head
        fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        start = slow.next
        slow.next = None
        pre = None
        cur = start
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        head2 = pre
        cur = dummy_head
        cur1 = head
        cur2 = head2
        while cur1 or cur2:
            if cur1:
                cur.next = cur1
                cur1 = cur1.next
                cur = cur.next
            if cur2:
                cur.next = cur2
                cur2 = cur2.next
                cur = cur.next
        return dummy_head.next



