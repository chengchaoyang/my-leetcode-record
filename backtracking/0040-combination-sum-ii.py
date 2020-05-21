"""
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次。

说明：
所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 

示例 1:
输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

示例 2:
输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        size = len(candidates)
        res = []
        if size == 0:
            return res

        def dfs(candidates,path,start,residue):
            if residue == 0:
                res.append(path[:])
                return
            for index in range(start,size):
                if residue < 0:
                    break
                #跳过第二个重复的数字，无需递归
                if index > start and candidates[index - 1] == candidates[index]:
                    continue
                path.append(candidates[index])
                dfs(candidates,path,index+1,residue - candidates[index])
                path.pop()

        candidates.sort()
        dfs(candidates,[],0,target)
        return res

candidates = [10,1,2,7,6,1,5]
target = 8
print(Solution().combinationSum2(candidates, target))
