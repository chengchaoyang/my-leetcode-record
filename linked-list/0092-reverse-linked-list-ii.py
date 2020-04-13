"""
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy_head = ListNode(-1)
        dummy_head.next = head
        cur_node = dummy_head
        for i in range(m-1):
            cur_node = cur_node.next
        begin = cur_node
        end = cur_node.next
        # 向前走一步
        cur_node = cur_node.next
        # 再前走一步
        pre = cur_node
        cur_node = cur_node.next
        for i in range(n-m):
            next = cur_node.next
            cur_node.next = pre
            pre = cur_node
            cur_node = next
        begin.next = pre
        end.next = cur_node
        return dummy_head.next


