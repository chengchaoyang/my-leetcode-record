"""
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
说明:

你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array

思路1：排序，然后返回倒数第 k 个元素，索引是 n−k；
思路2：partition ，逐渐减少搜索的范围，partition 的核心是大于等于的放过，小于的才做操作，因为要让小于的挪到前面去，
还能保证元素的相对位置不变； 注意一些边边角角的细节，+1 和 -1 要特别小心。
"""
from typing import List

class Solution:
    # 数组中的第 K 个最大元素
    # 数组中第 k 大的元素，它的索引是 len(nums) - k
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        size = len(nums)

        if size < k:
            raise Exception('程序出错')
            # [0,1,2,3,4,5]

        # 第 k 大元素的索引是 len(nums) - k
        left = 0
        right = len(nums) - 1

        while True:
            index = self.__partition(nums, left, right)
            if index == len(nums) - k:
                return nums[index]
            if index > len(nums) - k:
                right = index - 1
            else:
                left = index + 1

    def __partition(self, nums, left, right):
        """
        partition 是必须要会的子步骤，一定要非常熟练
        在 [left, right] 这个区间执行 partition
        遇到比第一个元素大的或等于的，就放过，遇到小的，就交换
        :param nums:
        :param left:
        :param right:
        :return:
        """
        pivot = nums[left]
        k = left
        for index in range(left + 1, right + 1):
            if nums[index] < pivot:
                k += 1
                nums[k], nums[index] = nums[index], nums[k]
        nums[left], nums[k] = nums[k], nums[left]
        return k

import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        size = len(nums)
        if k > size:
            raise Exception('程序出错')

        # 堆有序数组
        h = []

        for num in nums:
            if len(h) < k:
                heapq.heappush(h, num)
            else:
                if num < h[0]:
                    pass
                else:
                    heapq.heappushpop(h, num)
        return h[0]


if __name__ == '__main__':
    nums = [3, 7, 8, 1, 2, 4]
    solution = Solution()
    result = solution.findKthLargest(nums, 2)
    print(result)