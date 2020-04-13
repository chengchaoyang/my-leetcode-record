"""
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
你应当保留两个分区中每个节点的初始相对位置。

示例:

输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy_node1 = ListNode(-1)
        cur1 = dummy_node1
        dummy_node2 = ListNode(-1)
        cur2 = dummy_node2
        if head is None or head.next is None:
            return head
        cur = head
        while cur:
            if cur.val < x:
                cur1.next = cur
                cur1 = cur
            else:
                cur2.next = cur
                cur2 = cur
            cur = cur.next
        cur1.next = dummy_node2.next
        cur2.next = None
        return dummy_node1.next
        