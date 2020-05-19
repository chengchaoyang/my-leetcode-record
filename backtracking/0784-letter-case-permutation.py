"""
给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。

示例:
输入: S = "a1b2"
输出: ["a1b2", "a1B2", "A1b2", "A1B2"]

输入: S = "3z4"
输出: ["3z4", "3Z4"]

输入: S = "12345"
输出: ["12345"]

注意：
S 的长度不超过12。
S 仅由数字和字母组成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/letter-case-permutation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        size = len(S)
        if size == 0:
            return []

        res = []
        arr = list(S)
        self.__dfs(arr, size, 0, res)
        return res

    def __dfs(self, arr, size, start, res):
        if start == size:
            res.append(''.join(arr))
            return

        # 先把当前加到 pre 里面
        self.__dfs(arr, size, start + 1, res)

        # 如果是字母，就变换大小写
        if arr[start].isalpha():
            arr[start] = chr(ord(arr[start]) ^ (1 << 5))
            self.__dfs(arr, size, start + 1, res)

print(Solution().letterCasePermutation("C"))