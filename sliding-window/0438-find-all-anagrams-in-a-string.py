"""
给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。

说明：
字母异位词指字母相同，但排列不同的字符串。
不考虑答案输出的顺序。
示例 1:

输入:
s: "cbaebabacd" p: "abc"

输出:
[0, 6]

解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
 示例 2:

输入:
s: "abab" p: "ab"

输出:
[0, 1, 2]

解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-all-anagrams-in-a-string

思路1：滑动窗口的右边界划过的时候，map 对应的次数减少，左边界划过的时候，map 对应的次数增加。设置一个 distance 变量，表示二者的差距。
"""
from typing import List
from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        distance = len(p)
        #右指针往右，distance减小。左指针往左，distance增大，distance= 0，返回左指针位置
        res = []
        if len(s) < distance:
            return res
        counter = defaultdict(int)
        for j in p:
            counter[j] += 1
        l = 0
        for i in range(len(s)):

            if counter[s[i]] > 0:
                distance -= 1
            counter[s[i]] -= 1
            if distance == 0 and i - l == len(p):
                res.append(l)
            while distance <= 0 and l < i - len(p)+1:
                if counter[s[l]] >= 0:
                    distance += 1
                counter[s[l]] += 1
                l += 1
        return res


class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str 模式串
        :rtype: List[int]
        """

        from collections import defaultdict
        hash = defaultdict(int)
        # 滑动窗口的长度
        plen = len(p)
        # 预处理
        for alpha in p:
            hash[alpha] += 1
        # 滑动窗口的左边界
        l = 0
        # 滑动窗口的右边界
        r = 0

        res = []
        # 可以认为是两者的差距
        distance = plen

        while r < len(s):
            if hash[s[r]] > 0:
                distance -= 1
            hash[s[r]] -= 1
            r += 1
            if distance == 0:
                res.append(l)
            if r - l == plen:
                #不在p中的元素，个数为负数
                if hash[s[l]] >= 0:
                    distance += 1
                hash[s[l]] += 1
                l += 1
        return res


if __name__ == '__main__':
    s = "cbbbaebabacd"
    p = "abc"
    solution = Solution()
    result = solution.findAnagrams(s, p)
    print(result)

