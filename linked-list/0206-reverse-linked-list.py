"""
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        迭代法
        :param head:
        :return:
        """
        pre = None
        cur = head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        递归法
        递归实现与while实现不同在于递归首先找到新链表的头部节点，然后递归栈返回，层层反转
        首先找到新链表的头结点（即遍历到原链表的最后一个节点返回最后节点）
        执行函数体后续代码，将原链表中的尾节点指向原尾节点的前置节点
        前置节点的指针指向None(防止出现死循环)
        返回新链表的头部节点至上一层函数，重复以上操作
        :param head:
        :return:
        """
        if head is None or head.next is None:
            return head
        #保存下一个节点
        tmp = head.next
        new_head = self.reverseList(head.next)
        tmp.next = head
        head.next = None
        return new_head
