"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/move-zeroes
"""
from typing import List
class Solution:
    """
    思路：循环过程中，保持 [0, j) 这个区间中的元素非零，遍历一次就能够达到题目的要求。
    时间复杂度：O(n)；空间复杂度：O(1)。
    """
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                #nums[i]为非零
                nums[i],nums[j] = nums[j],nums[i]
                j += 1

if __name__ == "__main__":
    nums = [0,1,0,3,12]
    Solution().moveZeroes(nums)





