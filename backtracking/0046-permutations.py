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
from itertools import permutations
class Solution:
    """
    执行效率低，自己写的
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        result = []
        if size == 0:
            return result
        if size == 1:
            result.append(nums)
        preresult = self.permute(nums[:-1])
        num = nums[-1]
        for ori_res in preresult:
            for i in range(len(ori_res)+1):
                res = ori_res.copy() #由于insert会改变原始的数组，所以要copy对象
                res.insert(i,num)
                result.append(res)
        return result

class Solution:
    "库函数"
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(permutations(nums))

class Solution:
    """
    所谓全排列就是以每个nums中每个数字为起始位置，将剩余的数字全排列。所以可以使用递归求解。
    想解决递归问题，必须对函数的定义十分了解。代码中定义的dfs()是对nums进行全排列，
    已有的排列结果放到path中，当nums为空时说明递归完成，把path放入res中。
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, res, [])
        return res

    def dfs(self, nums, res, path):
        if not nums:
            res.append(path)
        else:
            for i in range(len(nums)):
                self.dfs(nums[:i] + nums[i + 1:], res, path + [nums[i]])

class Solution:
    """
    回溯法。
    回溯法是解决排列问题的经典方法，速度也能明显加快。
    回溯法的含义是对每个可能的结果进行遍历，如果某个数字已经使用则跳过，如果没有使用则放入path中。这个“回溯”怎么理解？
    我认识是在递归的过程中使用了一个数组path来保存自己走过的路，如果沿着这条路走完了全部的解，则需要弹出path中的最后一个元素，相当于向后回退，于是叫做回溯法。
    下面的做法中，使用了visited数组来保存是否经历过这个位置。
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = [0] * len(nums)
        res = []
        def dfs(path):
            if len(path) == len(nums):
                res.append(path)
            else:
                for i in range(len(nums)):
                    if not visited[i]:
                        visited[i] = 1
                        dfs(path + [nums[i]])
                        visited[i] = 0
        dfs([])
        return res

print(Solution().permute([1,2,3]))