"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例：
输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/generate-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List

class Solution:
    """
    做减法
    只要左括号还有剩余的数量，换句话说，只要左括号可以用，那么就可以在当前位置添加左括号；
    右括号的使用是有限制的，如果之前已经使用的左括号数量和右括号数量相等，那么当前就不能够使用右括号，
    原因我们刚刚也说了，如果使用了右括号，在之前就不能找到与之匹配的左括号。
    """
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur_str = ''

        def dfs(cur_str, left, right):
            """
            :param cur_str: 从根结点到叶子结点的路径字符串
            :param left: 左括号还可以使用的个数
            :param right: 右括号还可以使用的个数
            :return:
            """
            if left == 0 and right == 0:
                res.append(cur_str)
                return
            if right < left:
                return
            if left > 0:
                dfs(cur_str + '(', left - 1, right)
            if right > 0:
                dfs(cur_str + ')', left, right - 1)

        dfs(cur_str, n, n)
        return res

class Solution:
    """
    做加法
    """
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur_str = ''

        def dfs(cur_str, left, right):
            """
            :param cur_str: 从根结点到叶子结点的路径字符串
            :param left: 左括号还可以使用的个数
            :param right: 右括号还可以使用的个数
            :return:
            """
            if left == n and right == n:
                res.append(cur_str)
                return
            if right > left:
                return
            if left < n:
                dfs(cur_str + '(', left + 1, right)
            if right < n:
                dfs(cur_str + ')', left, right + 1)

        dfs(cur_str, 0, 0)
        return res

print(Solution().generateParenthesis(3))