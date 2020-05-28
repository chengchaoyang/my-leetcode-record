"""
累加数是一个字符串，组成它的数字可以形成累加序列。
一个有效的累加序列必须至少包含 3 个数。除了最开始的两个数以外，字符串中的其他数都等于它之前两个数相加的和。
给定一个只包含数字 '0'-'9' 的字符串，编写一个算法来判断给定输入是否是累加数。
说明: 累加序列里的数不会以 0 开头，所以不会出现 1, 2, 03 或者 1, 02, 3 的情况。

示例 1:
输入: "112358"
输出: true
解释: 累加序列为: 1, 1, 2, 3, 5, 8 。1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8

示例 2:
输入: "199100199"
输出: true
解释: 累加序列为: 1, 99, 100, 199。1 + 99 = 100, 99 + 100 = 199
进阶:
你如何处理一个溢出的过大的整数输入?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/additive-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        size = len(num)
        if size < 3:
            return False
        return self.__backtracking(num,0,size,[])

    def __backtracking(self,num,start,size,path):
        if len(path) >= 3 and  path[-3] + path[-2] == path[-1] and start == size:
            return True

        if len(path[:]) > 0 and path[:][-1] > int(num[start:]):
            return

        for i in range(1,size+1):
            num1 = num[start:start+i]
            if len(num1) > 1 and num1[0] == "0":
                continue
            if len(path) < 2:
                path.append(int(num1))
                print(path)
            else:
                if path[-2] + path[-1] == int(num1):
                    path.append(int(num1))
                    self.__backtracking(num,start+i,size,path)
                    path.pop()
        return False

num = "112358"
print(Solution().isAdditiveNumber(num))
