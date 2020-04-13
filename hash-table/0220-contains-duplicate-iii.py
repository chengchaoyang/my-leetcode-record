"""
给定一个整数数组，判断数组中是否有两个不同的索引 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值最大为 t，
并且 i 和 j 之间的差的绝对值最大为 ķ。

示例 1:
输入: nums = [1,2,3,1], k = 3, t = 0
输出: true

示例 2:
输入: nums = [1,0,1,1], k = 1, t = 2
输出: true

示例 3:
输入: nums = [1,5,9,1,5,9], k = 2, t = 3
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/contains-duplicate-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

思路1：二分去查找。
思路2：使用桶排序。

1、使用二分查找
2、使用树结构

* 使用了红黑树（一种特殊的二分查找树）的功能：查询天花板和地板，解决了这个问题。
由于 Python 中没有现成的 BST，因此得手写一个，这个 BST 要支持 floor 和 ceiling 操作。
"""

# 220. 存在重复元素 III
# 给定一个整数数组，判断数组中是否有两个不同的索引 i 和 j，
# 使得 nums [i] 和 nums [j] 的差的绝对值最大为 t，
# 并且 i 和 j 之间的差的绝对值最大为 ķ。

# 滑动窗口 + BST
from typing import List
class Solution:
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

    class bst:
        def __init__(self):
            self.root = None

        def __str__(self):
            # 中序遍历 bst
            s = ''
            if self.root is None:
                return ''
            stack = [(1, self.root)]

            while stack:
                type, node = stack.pop()
                if type == 0:
                    s += str(node.val) + ','
                else:
                    if node.right:
                        stack.append((1, node.right))
                    stack.append((0, node))
                    if node.left:
                        stack.append((1, node.left))
            return s[:-1]

        def insert(self, val):
            """
            将 val 插入 bst
            :param val:
            :return:
            """
            self.root = self.__insert(self.root, val)

        def __insert(self, node, val):
            # 在以 node 为根结点的 bst 中，插入 val
            if node is None:
                return Solution.TreeNode(val)
            if val < node.val:
                # 注意：不要写成 return self.__insert(node.left, val)
                node.left = self.__insert(node.left, val)
                return node
            elif val > node.val:
                # 注意：不要写成 return self.__insert(node.right, val)
                node.right = self.__insert(node.right, val)
                return node
            node.val = val
            # 注意：要把 node 返回回去
            return node

        def remove(self, val):
            """
            删除 bst 中等于 val 的结点
            :param val:
            :return:
            """
            if self.root:
                self.root = self.__remove(self.root, val)

        def __remove(self, node, val):
            #先找到该节点
            if node is None:
                return None
            if val < node.val:
                node.left = self.__remove(node.left, val)
                return node
            if val > node.val:
                node.right = self.__remove(node.right, val)
                return node

            if node.left is None:
                new_root = node.right
                node.right = None
                return new_root

            if node.right is None:
                new_root = node.left
                node.left = None
                return new_root

            # 用前驱结点 precursor 代替被删除结点
            precursor = self.__maximum(node.left)
            precursor_copy = Solution.TreeNode(precursor.val)
            precursor_copy.left = self.__remove_max(node.left)
            precursor_copy.right = node.right
            node.left = None
            node.right = None
            return precursor_copy

        def __maximum(self, node):
            while node.right:
                node = node.right
            return node

        def __remove_max(self, node):
            if node.right is None:
                new_root = node.left
                node.left = None
                return new_root
            node.right = self.__remove_max(node.right)
            return node

        def floor(self, val):
            return self.__floor(self.root, val)

        def __floor(self, node, val):
            """
            找比val小的node
            是最接近key值且**小于**key的节点
            如果node的key值和要寻找的key值相等：则node本身就是key的floor节点。
            如果node的key值比要寻找的key值大：则要寻找的key的floor节点一定在node的左子树中。
            如果node的key值比要寻找的key值小：则node有可能是key的floor节点, 也有可能不是(
            存在比node->key大但是小于key的其余节点)，需要尝试向node的右子树寻找一下。
            :param node:
            :param val:
            :return:
            """
            if node is None:
                return None
            if node.val == val:
                return node.val
            if val < node.val:
                return self.__floor(node.left, val)
            temp_val = self.__floor(node.right, val)
            if temp_val:
                return temp_val
            return node.val

        def ceiling(self, val):
            return self.__ceiling(self.root, val)

        def __ceiling(self, node, val):
            """
            是最接近key值且**大于**key的节点
            如果node的key值和要寻找的key值相等：则node本身就是key的floor节点。
            如果node的key值比要寻找的key值小：则要寻找的key的ceil节点一定在node的右子树中。
            如果node的key值比要寻找的key值大：则node有可能是key的ceil节点, 也有可能不是(
            存在比node->key大但是小于key的其余节点)，需要尝试向node的左子树寻找一下。
            :param node:
            :param val:
            :return:
            """
            if node is None:
                return None
            if node.val == val:
                return node.val
            if val > node.val:
                return self.__ceiling(node.right, val)
            temp_val = self.__ceiling(node.left, val)
            if temp_val:
                return temp_val
            return node.val

    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        # 思路：滑动窗口

        size = len(nums)
        if size <= 1 or k <= 0:
            return False
        bst = Solution.bst()

        for i in range(size):
            # 体会这个过程：我先查询一次，就好像这个数我放到 bst 中一样
            # 如果符合题意，就直接返回了
            # 如果不符合题意，移除最左边的元素，放入当前遍历的元素

            floor = bst.floor(nums[i])
            if floor is not None and nums[i] - floor <= t:
                return True

            ceiling = bst.ceiling(nums[i])
            if ceiling is not None and ceiling - nums[i] <= t:
                return True
            # 注意这里：先移除最左边的，然后插入
            # 或者先加入，再移除最左边的，其实都可以
            # 总之要保证
            if i >= k:
                bst.remove(nums[i - k])
            bst.insert(nums[i])

        return False


if __name__ == '__main__':
    nums = [8, 4, 0, 2]
    # nums = [1, 5, 8, 14, 19, 24, 37, 48]
    k = 2  # 索引差
    t = 2  # 数值差

    solution = Solution()
    result = solution.containsNearbyAlmostDuplicate(nums, k, t)
    print(result)

    # bst = Solution.bst()
    # bst.insert(12)
    # bst.insert(15)
    # bst.insert(11)
    # bst.insert(6)
    # bst.insert(14)
    # bst.insert(18)
    # bst.insert(9)
    #
    # print(bst)
    # bst.remove(12)
    # print(bst)
    #
    # f = bst.floor(5)
    # print(f)
    #
    # c = bst.ceiling(17)
    # print(c)