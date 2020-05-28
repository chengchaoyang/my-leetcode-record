"""
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
有效的 IP 地址正好由四个整数（每个整数位于 0 到 255 之间组成），整数之间用 '.' 分隔。

示例:

输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/restore-ip-addresses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        size = len(s)
        # 剪枝操作，大于 12 的直接不考虑
        if size == 0 or size > 12:
            return []

        res = []
        path = []
        splits = 0

        self.__backtracking(s, 0, size, splits, path, res)
        return res

    def __backtracking(self, s, begin, size, splits, path, res):
        if splits == 4 and begin == size:
            res.append('.'.join(path))
            return

        # 重要操作：剪枝,size - begin 剩余的字符串，4 - splits剩余的组数
        remain_chars = size - begin
        remain_splits = 4 - splits
        if remain_chars < remain_splits or remain_chars > 3*remain_splits:
            return
        # if size - begin < (4 - splits) or size - begin > 3 * (4 - splits):
        #     return

        for i in range(1, 4):
            # 注意：这里是严格大于号，看 s[begin:begin + i] 表达式就清楚
            if begin + i > size:
                break
            ip_segment = s[begin:begin + i]
            if self.__judge_ip_segment(ip_segment):
                path.append(ip_segment)
                self.__backtracking(s, begin + i, size, splits + 1, path, res)
                path.pop()

    def __judge_ip_segment(self, ip_segment):
        if len(ip_segment) > 1 and ip_segment[0] == '0':
            return False
        return int(ip_segment) <= 255

if __name__ == '__main__':
    s = "25525511135"
    solution = Solution()
    res = solution.restoreIpAddresses(s)
    print(res)


