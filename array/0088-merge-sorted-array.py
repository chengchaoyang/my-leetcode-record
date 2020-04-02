"""
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 num1 成为一个有序数组。

说明:
初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

示例:
输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]
https://leetcode-cn.com/problems/merge-sorted-array/
"""
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums3 = nums1.copy()
        k = 0 #下一个要比较的索引
        j = 0
        for i in range(m+n):
            if k > m-1:
                nums1[i] = nums2[j]
                j += 1
            elif j > n-1:
                nums1[i] = nums3[k]
                k+= 1
            elif nums3[k] <= nums2[j]:
                nums1[i] = nums3[k]
                k += 1
            else:
                nums1[i] = nums2[j]
                j += 1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
Solution().merge(nums1,m,nums2,n)

