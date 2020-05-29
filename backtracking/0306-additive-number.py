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
    """
    有bug，dfs
    """
    def isAdditiveNumber(self, num: str) -> bool:
        size = len(num)
        if size < 3:
            return False
        res = []
        self.__backtracking(num,0,size,[],res)
        return len(res) == 1

    def __backtracking(self,num,start,size,path,res):
        if len(path) >= 3 and path[-3] + path[-2] == path[-1] and start == size:
            print(path)
            res.append(True)
            #return
        if len(path) > 0 and start < size:
            if path[-1] > int(num[start:]):
                return

        for i in range(1,size):
            if len(res) > 0:
                break
            if start >= size:
                continue
            num1 = num[start:start+i]
            if len(num1) > 1 and num1[0] == "0":
                continue
            if len(path) == 0:
                path.append(int(num1))
            print(path)
            if len(path) == 1:
                for j in range(1,size):
                    num2 = num[start+i:start+i+j]
                    if len(num2) > 1 and num2[0] == "0":
                        continue
                    path.append(int(num2))
                    self.__backtracking(num, start + i + j, size, path, res)
                    path.pop()

            if len(path) >= 2 and path[-2] + path[-1] == int(num1):
                path.append(int(num1))
                self.__backtracking(num,start+i,size,path,res)
                path.pop()



class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        size = len(num)
        return self.__backtracking(num, 0, size, 0, 0, 0)

    def __backtracking(self, num, start, size, pre_sum, cur_num, split):
        if split > 2 and start == size:
            return True

        for i in range(0, size - start):
            new_num = self.__calculate_new_num(num, start, start + i, pre_sum, split)
            # 这里判断得是大于等于 0，特例 "1,0,1"
            if new_num >= 0:
                if self.__backtracking(num, start + i + 1, size, cur_num + new_num, new_num, split + 1):
                    return True
        return False

    def __calculate_new_num(self, num, left, right, pre_sum, split):
        if left < right and num[left] == '0':
            return -1

        cur_num = 0
        while left <= right:
            cur_num = (cur_num * 10 + ord(num[left]) - ord('0'))
            left += 1

        if split < 2:
            return cur_num

        if pre_sum == cur_num:
            return cur_num
        return -1


class Solution(object):
    """
    因为只要判断能否构成即可，所以不需要res数组保存结果。回溯法仍然是对剩余的数字进行切片，看该部分切片能否满足条件。
    剪枝的方法是判断数组是否长度超过3，如果超过那么判断是否满足费布拉奇数列的规则。不超过3或者已经满足的条件下继续进行回溯切片。
    最后当所有的字符串被切片完毕，要判断下数组长度是否大于等于3，这是题目要求。

    """
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        return self.dfs(num, [])

    def dfs(self, num_str, path):
        if len(path) >= 3 and  path[-1] != path[-2] + path[-3]:
            return False
        if not num_str and len(path) >= 3:
            return True
        for i in range(len(num_str)):
            curr = num_str[:i+1]
            if (curr[0] == '0' and len(curr) != 1):
                continue
            if self.dfs(num_str[i+1:], path + [int(curr)]):
                return True
        return False


num = "1023"
#num = "199100199"
print(Solution().isAdditiveNumber(num))
