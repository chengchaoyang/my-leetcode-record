"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 用指针对撞的方式
            l = i + 1
            r = len(nums) - 1
            # 不能等于，等于就变成取一样的数了
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    # 注意：这一步在去重，是第一种解法 set 做不到的
                    # 看一看右边是不是和自己相等，如果相等，就向右边移动一格
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    # 看一看左边是不是和自己相等，如果相等，就向右边移动一格
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res

class Solution(object):
    # 排序可以去掉 -4 但是不能把后面重复的 2 去掉
    # [-4,-4,2,2]
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()

        # 特判
        if nums[0] == nums[-1] == 0:
            return [[0, 0, 0]]

        res = set()
        # 最后两个数就没有必要作为遍历的起点了
        for index, one in enumerate(nums[:-2]):
            # 因为题目要求，答案中不可以包含重复的三元组。
            if index >= 1 and nums[index] == nums[index - 1]:
                continue
            s = set()
            for two in nums[index + 1:]:
                if two not in s:
                    s.add(-one - two)
                else:
                    # 找到了一个解
                    res.add((one, two, -one - two))
        return list(map(list, res))