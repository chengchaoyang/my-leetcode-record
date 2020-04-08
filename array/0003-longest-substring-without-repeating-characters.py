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
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = {}
        max_size = 0
        begin = -1
        for i,t in enumerate(s):
            if t not in hash:
                max_size = max(i - begin, max_size)
            else:
                begin = hash[t]+1
                max_size = max(i - begin, max_size)
            hash[t] = i
            print(max_size)
            print(hash)
        return max_size


s =  "abba"
print(Solution().lengthOfLongestSubstring(s))