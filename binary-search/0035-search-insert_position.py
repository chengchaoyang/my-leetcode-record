"""
链接：https://leetcode-cn.com/problems/search-insert-position/
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
"""
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        size = len(nums)
        if size == 0:
            return 0
        l = 0
        r = size
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l

if __name__ == "__main__":
    nums = [1,3,5,6]
    target = 1
    print(Solution().searchInsert(nums,target))