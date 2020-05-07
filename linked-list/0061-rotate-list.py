"""
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:
输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL

示例 2:
输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    自己写的解法，需要遍历两次链表，第一次获取链表长度，根据k值，来找到新的链表头
    """
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or k <= 0:
            return head
        size = 1
        cur = head
        while cur.next:
            cur = cur.next
            size += 1
        k = k % size
        cur.next = head
        cur = head
        for _ in range(size - k -1):
            cur = cur.next
        new_head = cur.next
        cur.next = None
        return new_head



a = ListNode(0)
b = ListNode(1)
c = ListNode(2)
a.next = b
b.next = c
d = Solution().rotateRight(a,4)
cur = d
while cur:
    print(cur.val)
    cur = cur.next