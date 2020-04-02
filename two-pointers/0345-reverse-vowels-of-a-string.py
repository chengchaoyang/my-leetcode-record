"""
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

示例 1:
输入: "hello"
输出: "holle"

示例 2:
输入: "leetcode"
输出: "leotcede"
说明:
元音字母不包含字母"y"。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-vowels-of-a-string
"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a","e","i","o","u"]
        size = len(s)
        s = list(s)
        if size == 0:
            return ""
        l = 0
        r = size - 1
        while l < r:
            if s[l].lower() in vowels and s[r].lower() in vowels:
                s[l],s[r] = s[r],s[l]
                l += 1
                r -= 1
            if s[l].lower() not in vowels:
                l += 1
            if s[r].lower() not in vowels:
                r -= 1
        return "".join(s)

s = "Euston saw I was not Sue."
print(Solution().reverseVowels(s))
