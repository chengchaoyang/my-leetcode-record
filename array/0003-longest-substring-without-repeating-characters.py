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
        滑窗法求解
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

s =  "abba"
print(Solution().lengthOfLongestSubstring(s))