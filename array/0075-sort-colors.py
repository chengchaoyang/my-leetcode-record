"""
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:
输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]

进阶：
一个直观的解决方案是使用计数排序的两趟扫描算法。
首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
你能想出一个仅使用常数空间的一趟扫描算法吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-colors
"""
from collections import defaultdict
from typing import List
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        counter = [0] * 3
        for num in nums:
            counter[num] += 1

        i = 0
        for _ in range(counter[0]):
            nums[i] = 0
            i += 1
        for _ in range(counter[1]):
            nums[i] = 1
            i += 1
        for _ in range(counter[2]):
            nums[i] = 2
            i += 1

class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        counter = [0] * 3
        for num in nums:
            counter[num] += 1
        i = 0
        for idx, count in enumerate(counter):
            for _ in range(count):
                nums[i] = idx
                i += 1

class Solution:
    "三路快排，[0,k) , [k,j], (j,-1]"
    def sortColors(self, nums):
        k = 0
        j = len(nums) - 1
        for i in range(len(nums)):
            print(nums)
            if nums[i] == 0:
                nums[i],nums[k] = nums[k],nums[i]
                k += 1
            elif nums[i] == 2:
                nums[i],nums[j] = nums[j],nums[i]
                j -= 1
        return nums

class Solution:
    def sortColors(self, nums):
        l = len(nums)

        # 循环不变量的定义：
        # [0, zero] 中的元素全部等于 0
        # (zero, i) 中的元素全部等于 1
        # [two, l - 1] 中的元素全部等于 2
        zero = -1
        two = l
        i = 0  # 马上要看的位置

        while i < two:
            print(i,nums)
            if nums[i] == 0:
                zero += 1
                nums[zero], nums[i] = nums[i], nums[zero]
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                two -= 1
                nums[two], nums[i] = nums[i], nums[two]

nums = [2,0,2,1,1,2]
print(Solution().sortColors(nums))