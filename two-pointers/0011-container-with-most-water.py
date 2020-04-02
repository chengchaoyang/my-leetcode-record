"""
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
说明：你不能倾斜容器，且 n 的值至少为 2。

 
图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

示例：
输入：[1,8,6,2,5,4,8,3,7]
输出：49

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/container-with-most-water
"""
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        思路：贪心算法，总是贪心先固定容器的宽度。根据木桶原理（盛水的高度由最短的那块木板决定），
        高的那块木板往里面走，只可能让盛水越来越少，但是短板往里面走，却有可能让盛水越来越多。
        :param height:
        :return:
        """
        l = 0
        r = len(height) - 1
        res = 0
        while l < r:
            min_h = min(height[l], height[r])
            res = max(res, (r - l) * min_h)
            if min_h == height[l]:
                l += 1
            else:
                r -= 1
        return res


