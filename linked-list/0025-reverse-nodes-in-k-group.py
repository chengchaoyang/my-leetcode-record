"""
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
k 是一个正整数，它的值小于或等于链表的长度。
如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

示例：
给你这个链表：1->2->3->4->5
当 k = 2 时，应当返回: 2->1->4->3->5
当 k = 3 时，应当返回: 3->2->1->4->5

说明：
你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-nodes-in-k-group
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # 定义一个哨兵节点
        sentry = ListNode(0)
        pre = sentry
        start = head
        flag = True
        while head:
            for i in range(k):
                if not head:
                    # 剩余节点数量小于k，跳出
                    flag = False
                    break
                head = head.next
            if not flag:
                break
            # 上次翻转后的节点连接这次翻转后的节点
            pre.next = self.reverse(start,head)
            # 连接这次翻转以后的正常节点
            start.next = head
            # 更新位置
            pre = start
            # 更新位置
            start = head
        return sentry.next

    def reverse(self,start,end):
        pre, cur, nexts = None, start, start
        # 三个指针进行局部翻转
        while cur != end:
            nexts = nexts.next
            # 箭头反指
            cur.next = pre
            # 更新pre位置
            pre = cur
            # 更新cur位置
            cur = nexts
        return pre

