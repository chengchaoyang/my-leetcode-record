"""
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个
重复的整数，找出这个重复的数。

示例 1:

输入: [1,3,4,2,2]
输出: 2
示例 2:

输入: [3,1,3,4,2]
输出: 3
说明：

不能更改原数组（假设数组是只读的）。
只能使用额外的 O(1) 的空间。
时间复杂度小于 O(n2) 。
数组中只有一个重复的数字，但它可能不止重复出现一次。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-duplicate-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        size = len(nums)
        left = 1
        right = size - 1

        while left < right:
            mid = (left + right + 1) >> 1
            print(mid)

            cnt = 0
            for num in nums:
                if num < mid:
                    cnt += 1
            # 根据抽屉原理，严格小于 4 的数的个数如果大于等于 4 个，
            # 此时重复元素一定出现在 [1, 3] 区间里

            if cnt >= mid:
                # 重复的元素一定出现在 [left, mid - 1] 区间里
                # 那么重复的数一定位于 1、2、3
                right = mid - 1
            else:
                # if 分析正确了以后，else 搜索的区间就是 if 的反面
                # [mid, right]
                # 注意：此时需要调整中位数的取法为上取整
                left = mid
        return left

nums = [3,1,3,4,2]
print(Solution().findDuplicate(nums))