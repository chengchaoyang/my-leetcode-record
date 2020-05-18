"""
给定一个 没有重复 数字的序列，返回其所有可能的全排列。
示例:

输入: D
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        result = []
        if size == 0:
            return result
        num = nums[-1]
        preresult = self.permute(nums[:-1])
        for res in preresult:
            for i in range(len(res)+1):
                res.insert(i,num)
                result.append(res)
        return result


print(Solution().permute([1,2,3]))