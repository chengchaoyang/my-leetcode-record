"""
链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array

1、循环可以继续的条件是 l < r，这样退出循环的时候 l == r 成立，因此就不用纠结返回 l 还是 r 了；
不过要特别注意一点：我们是通过夹逼的方式把搜索的范围逼到一个点，那么这个点是不是符合要求还要单独做判断。
2、循环体比较简单，真正地做到了“二分”，即“写两个分支”作判断，只要分支条件写正确，其中一个分支一定可以排除掉中点，而另一个分支则保留了中点；
3、取“中点”的操作有 2 种，根据循环体的收缩情况，采用合适的中点方法，这一点很重要，否则会出现死循环。

（1）mid = l + (r - l) // 2，特点：在只有两个数的时候，靠近左边。
（2）mid = l + (r - l + 1) // 2，特点：在只有两个数的时候，靠近右边。

例如：循环体是 l = mid + 1 和 r = mid 的时候，表示左端点不断右移，则选择（1），否则会出现死循环；

循环体是 l = mid 和 r = mid - 1 的时候，表示右端点不断左移，则选择（2），否则会出现死循环。
"""
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return -1
        lower = self.__get_lower(nums,target)
        if lower == -1:
            return [-1,-1]
        upper = self.__get_upper(nums,target)
        return [lower,upper]

    def __get_upper(self,nums,target):
        """
        右端点不断左移，选取靠右的中位数，否则会出现死循环
        :param nums:
        :param target:
        :return:
        """
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + (r - l + 1) // 2
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid
        if nums[l] == target:
            return l
        return -1

    def __get_lower(self,nums,target):
        """
        左端点不断右移，选取靠左的中位数，否则会出现死循环
        :param nums:
        :param target:
        :return:
        """
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + (r - l ) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        if nums[l] == target:
            return l
        return -1

if __name__ == "__main__":
    nums = [5,7,7,8,8,10]
    target = 7
    print(Solution().searchRange(nums,target))