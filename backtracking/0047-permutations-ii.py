"""
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:
输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.helper(nums, res, [])
        return res

    def helper(self, nums, res, path):
        if not nums and path not in res:
            res.append(path)
        else:
            for i in range(len(nums)):
                self.helper(nums[:i] + nums[i + 1:], res, path + [nums[i]])


class Solution(object):
    """
    如何去重呢？我们想一想为什么会有重复出现：在这个例子中，我们在第一个1开始的排列中已经取了第二个1的情况；
    如果在第二个1开始的排列中仍然取第一个1，就有重复了。所以，我们的做法是先对数组进行排序，保证相等的数字放在一起，
    然后当我们遇到的不是第一个数字，并且现在的数字和前面的数字相等，同时前面的数字还没有访问过，我们是不能搜索的，
    需要直接返回。原因是，这种情况下，必须是由前面搜索到现在的这个位置，而不能是由现在的位置向前面搜索。
    """
    def permuteUnique(self, nums):
        def dfs(nums, size, path, used, res):
            if len(path) == size:
                res.append(path[:])
                return
            for i in range(size):
                if not used[i]:
                    if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                        continue

                    used[i] = True
                    path.append(nums[i])
                    dfs(nums, size, path, used, res)
                    used[i] = False
                    path.pop()

        size = len(nums)
        if size == 0:
            return []

        nums.sort()

        used = [False] * len(nums)
        res = []
        dfs(nums, size, [], used, res)
        return res

print(Solution().permuteUnique([1,1,1,2]))