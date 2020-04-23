"""
对链表进行插入排序。
插入排序的动画演示如上。从第一个元素开始，该链表可以被认为已经部分排序（用黑色表示）。
每次迭代时，从输入数据中移除一个元素（用红色表示），并原地将其插入到已排好序的链表中。

插入排序算法：
插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
重复直到所有输入数据插入完为止。

示例 1：
输入: 4->2->1->3
输出: 1->2->3->4

示例 2：
输入: -1->5->3->4->0
输出: -1->0->3->4->5
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    超出时间限制
    """
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        dummy_node = ListNode(-1)
        dummy_node.next = ListNode(head.val)
        cur = head.next
        while cur:
            #print(cur.val)
            sort_node = dummy_node
            insert_node = ListNode(cur.val)
            while sort_node.next:
                if sort_node.next.val > cur.val:
                    # 会发生死循环,先修改了dummy_node的下一个指针的值，sort_node.next就会一直是修改后的值，造成死循环
                    # dummy_node.next = insert_node
                    # insert_node.next = sort_node.next
                    insert_node.next = sort_node.next
                    dummy_node.next = insert_node
                    break
                else:
                    if sort_node.next.next:
                        nexts = sort_node.next.next
                        if cur.val <= nexts.val:
                            insert_node.next = nexts
                            sort_node.next.next = insert_node
                            break
                        else:
                            sort_node = sort_node.next
                            #print(sort_node.val)
                    else:
                        sort_node.next.next = insert_node
                        break
            cur = cur.next
        return dummy_node.next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        dummy_node = ListNode(-1)
        dummy_node.next = head
        cur = head
        while True:
            #  如果遍历下去，是顺序排列的话，那最简单了，curNode
            # 指针向前就行了
            #  这一步是一个循环的过程
            #  暂存当前结点的下一结点
            while cur.next != None and cur.val <= cur.next.val:
                cur = cur.next
            if cur.next == None:
                break
            else:
                #否则就一定满足 curNode.val > curNode.next.val; 为真
                #  pre 打回到起点
                pre = dummy_node
                next = cur.next
                while pre.next.val < next.val:
                    pre = pre.next
                #穿针引线
                cur.next = next.next
                next.next = pre.next
                pre.next = next
        return dummy_node.next




a = ListNode(-1)
b = ListNode(5)
c = ListNode(3)
d = ListNode(4)
f = ListNode(0)
a.next = b
b.next = c
c.next = d
d.next = f
print(a)
e = Solution().insertionSortList(a)
cur = e
while cur:
    print(cur.val)
    cur = cur.next