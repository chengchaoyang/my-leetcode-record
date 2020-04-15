"""
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
示例 1:

输入: 1->2->3->3->4->4->5
输出: 1->2->5
示例 2:

输入: 1->1->1->2->3
输出: 2->3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        if head.next:
            if head.val != head.next.val:
                head.next = self.deleteDuplicates(head.next)
            else:
                cur = head
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                head = self.deleteDuplicates(cur.next)
        return head


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None or head.next is None:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy

        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                # 继续往后看，有没有相等的元素
                # del_node 至少删掉它
                del_node = cur.next.next
                while del_node.next and del_node.val == del_node.next.val:
                    del_node = del_node.next
                # 开始删除操作
                cur.next = del_node.next
                del_node.next = None
            else:
                cur = cur.next
        return dummy.next