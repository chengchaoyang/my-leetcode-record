"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        res = []
        if size == 0:
            return res
        self.dfs(nums,size,0,[],res)
        return res

    def dfs(self,nums,size,start,path,res):
        res.append(path[:])
        for index in range(start,size):
            path.append(nums[index])
            self.dfs(nums,size,index+1,path,res)
            path.pop()


nums = [1,2,3]
print(Solution().subsets(nums))