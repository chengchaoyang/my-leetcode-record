"""
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。

示例: 
输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。

进阶:
如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-size-subarray-sum

思路1：使用滑动窗口的技巧来完成，要看过一遍整个数组的元素，时间复杂度是 O(n)。要求满足区间和 >= s 的最小子区间的长度，因此，我们从左向右进行扫描。
情况1：当区间和小于 s 的时候，右区间的端点向右扩展，这一点依赖外层循环的遍历就可以完成；
情况2：一旦区间和大于等于 s，尝试一步一步缩小左区间端点，看看是否能得到一个更短的区间，满足区间和 >=s，这一步通过一个内层循环实现。
"""
from typing import List

class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # 滑动窗口
        size = len(nums)
        # 特判
        if size == 0:
            return 0

        l = 0

        # 既然是求最小的长度，初始值应该设置成一个不可能达到的上限
        res = size + 1
        cur_sum = 0
        for i in range(size):
            cur_sum += nums[i]
            # 此时 cur_sum >= s
            while cur_sum >= s:
                res = min(res, i - l + 1)
                cur_sum -= nums[l]
                l += 1
        # 如果全部数组元素加起来都 < s ，即 res 的值没有被更新，根据题意返回 0
        if res == len(nums) + 1:
            return 0
        return res

class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # 滑动窗口
        size = len(nums)
        # 特判
        if size == 0:
            return 0

        l = 0
        r = -1
        sum = 0
        res = size + 1
        while l < size:
            if r + 1 < size and sum < s:
                r += 1
                sum += nums[r]
            else:
                sum -= nums[l]
                l += 1
            if sum >= s:
                res = min(res, r - l + 1)
        if res == size + 1:
            return 0
        return res

s = 11
nums = [1,2,3,4,5]
print(Solution().minSubArrayLen(s,nums))