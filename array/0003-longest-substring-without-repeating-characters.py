"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # 特判
        size = len(s)
        if size < 2:
            return size

        l = 0
        r = -1

        counter = [0 for _ in range(256)]

        res = 1
        while l < size:
            if r + 1 < size and counter[ord(s[r + 1])] == 0:
                # 表示没有重复元素，r 可以加 1
                counter[ord(s[r + 1])] += 1
                r += 1
            else:
                # 有重复元素，左边就要减 1
                counter[ord(s[l])] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 特判
        l = len(s)
        if l < 2:
            return l
        # 隔板法
        # key:字符，val 出现的索引
        map = dict()
        point = 0
        res = 1
        for i in range(l):
            # 关键1：map[s[i]] >= point，等于是可以的
            if s[i] in map and map[s[i]] >= point:
                # 先把隔板向后移动一位
                point = map[s[i]] + 1
            # 然后记录最长不重复子串的长度
            res = max(res, i - point + 1)
            # 关键2：无论如何都更新位置
            map[s[i]] = i
        return res

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 特判
        l = len(s)
        if l < 2:
            return l
        # dp[i] 表示以 s[i] 结尾的最长不重复子串的长度
        # 因为自己肯定是不重复子串，所以初始值设置为 1
        dp = [1 for _ in range(l)]
        map = dict()
        map[s[0]] = 0
        for i in range(1, l):
            if s[i] in map:
                if i - map[s[i]] > dp[i - 1]:
                    dp[i] = dp[i - 1] + 1
                else:
                    dp[i] = i - map[s[i]]
            else:
                dp[i] = dp[i - 1] + 1
            # 设置字符与索引键值对
            map[s[i]] = i
        # 最后拉通看一遍最大值
        return max(dp)

s =  "abba"
print(Solution().lengthOfLongestSubstring(s))