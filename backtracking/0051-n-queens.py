"""
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
即任意两个皇后都不能处于同一行、同一列或同一斜线上

上图为 8 皇后问题的一种解法。
给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例:

输入: 4
输出: [
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
解释: 4 皇后问题存在两个不同的解法。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-queens
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

class Solution:
    """
    规则不对，错误解法
    """
    def solveNQueens(self, n: int) -> List[List[str]]:
        global res
        res = 0
        if n == 0:
            return res
        if n == 1:
            return 1
        if n == 2:
            return res

        def dfs(n,path):
            if len(path) == n and abs(path[-1] - path[-2]) > 1:
                global res
                res += 1
                return
            for index in range(n):
                if index in path :
                    continue
                path.append(index)
                dfs(n, path)
                path.pop()
        dfs(n,[])
        return res

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        if n == 0:
            return res
        columns = [-1 for _ in range(n)]
        self.dfs(n,0,res,columns)
        return res

    def check(self,row,column,columns):
        for i in range(row):
            if column == columns[i] or row - i == abs(columns[i] - column):
                return False
        return True

    def dfs(self,n,row,res,columns):
        if row == n:
            path = ["."*i +"Q" + "."*(len(columns)-1-i) for i in columns]
            res.append(path)
            return
        for column in range(n):
            if self.check(row,column,columns):
                columns[row] = column
                self.dfs(n,row+1,res,columns)
                columns[row] = -1

print(Solution().solveNQueens(8))
