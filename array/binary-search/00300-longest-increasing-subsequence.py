"""
给定一个无序的整数数组，找到其中最长上升子序列的长度。
示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
"""
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        increasing_seq = [nums[0]]
        for i in range(1,len(nums)):
            pre_num = increasing_seq[-1]
            if nums[i] > pre_num:
                increasing_seq.append(nums[i])
            else:
                insert_index = self.__insert_position(increasing_seq,nums[i])
                increasing_seq[insert_index] = nums[i]
        return len(increasing_seq)

    def __insert_position(self,seq,target):
        l = 0
        r = len(seq) - 1
        while l < r:
            mid = l + (r - l) // 2
            if seq[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size < 2:
            return size
        # 最长上升子序列
        tail = []
        for num in nums:
            # 找到大于等于 num 的第 1 个数
            left = 0
            # 因为有可能新加的这个数，比之前所有的数都大，所以右边界是当前 tail 的长度
            right = len(tail)
            while left < right:
                mid = (left + right) >> 1
                if tail[mid] >= num:
                    right = mid
                else:
                    left = mid + 1
            if left == len(tail):
                tail.append(num)
            else:
                # 大于等于 num 的第 1 个数变小
                # 这样后面才有可能接上更多的数，是贪心算法的思想
                tail[left] = num
        return len(tail)

if __name__ == "__main__":
    nums = [10,9,2,5,3,7,101,18]
    print(Solution().lengthOfLIS(nums))