"""
给定平面上 n 对不同的点，“回旋镖” 是由点表示的元组 (i, j, k) ，其中 i 和 j 之间的距离和 i 和 k 之间的距离相等（需要考虑元组的顺序）。

找到所有回旋镖的数量。你可以假设 n 最大为 500，所有点的坐标在闭区间 [-10000, 10000] 中。

示例:

输入:
[[0,0],[1,0],[2,0]]

输出:
2

解释:
两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-boomerangs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
class Solution:
    def numberOfBoomerangs(self, points):
        import math
        res = 0
        size = len(points)
        d = dict()

        for i in range(size):
            for j in range(size):
                if i != j:

                    distance = math.pow(points[i][0] - points[j][0], 2) + math.pow(points[i][1] - points[j][1], 2)
                    if distance in d:
                        n = d[distance]
                        res += 2 * n
                        d[distance] = (n + 1)
                    else:
                        d[distance] = 1
            d.clear()
        return res

if __name__ == '__main__':
    points = [[0, 0], [1, 0], [2, 0]]
    solution = Solution()
    res = solution.numberOfBoomerangs(points)
    print(res)

