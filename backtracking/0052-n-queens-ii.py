"""
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
上图为 8 皇后问题的一种解法。
给定一个整数 n，返回 n 皇后不同的解决方案的数量。

示例:
输入: 4
输出: 2

解释: 4 皇后问题存在如下两个不同的解法。
[
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
 

提示：

皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。
当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一或七步，可进可退。
（引用自 百度百科 - 皇后 ）

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-queens-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def totalNQueens(self, n: int) -> int:
        global res
        res = 0
        if n == 0:
            return res
        columns = [-1 for _ in range(n)]
        self.backtracking(n,0,columns)
        return res

    def check(self,row,column,columns):
        for i in range(row):
            if columns[i] == column or row - i == abs(columns[i] - column):
                return False
        return True

    def backtracking(self,n,row,columns):
        if row == n:
            global res
            res += 1
            return
        for i in range(n):
            if self.check(row,i,columns):
                columns[row] = i
                self.backtracking(n,row+1,columns)
                columns[row] = -1

print(Solution().totalNQueens(4))