"""
“10个小球随机分到12个盒子里，求恰好10个盒子都为空的概率，要求用 Python 程序模拟十万次，
暴力求出该概率。


每个球都有12种放法,10个球共有12^10种放法
只有两个2盒子有球的放法是先在12个盒子中选2个,然后放10个球,每个球有2种方法,共有 12C2 * 2^10
除一下就可以了.
C(12,2)*((2/12)^10-2*(1/12)^10)

字节跳动面试题
"""
import math
#
# def permutation_combination(upper,lower):
#     """
#     :param num: int
#     :return: 排列组合
#     """
#     #分子
#     numerator = 1
#     #分母
#     denominator = 1
#     for i in range(1,upper+1):
#         numerator *= i
#     for j in range(1,lower+1):
#         denominator *= j
#     for j in range(1,upper - lower +1):
#         denominator *= j
#     return numerator/denominator
#
# def helper(ball,empty):
#     """
#     把几个球放到几个空位的方法数
#     :param ball: 要放置的球个数
#     :param empty: 有几个空位可以放置
#     :return: 一共有多少方法可以放置
#     """
#     count = 0
#     if empty == 0:
#         return 0
#     if empty == 1 and ball > 0:
#         return 1
#     for i in range(1,ball-empty+2):
#         count+=helper(ball-i,empty-1)
#     return count
#
# # print(helper(5,3))
# def probabity(box,ball):
#     #10个空盒子发生的次数
#     # C(12,10) *
#     numerator = permutation_combination(box,ball)*helper(ball,box-ball)
#     #2到11个空盒子发生的次数
#     denominator = 0
#     for i in range(box-ball,box):
#         denominator += permutation_combination(box,i)*helper(ball,box-i)
#         #print(i,permutation_combination(box,i)*helper(ball,box-i))
#     return numerator / denominator
#
# print(probabity(12,10))
# import random
# from collections import Counter
# box = 12
# ball = 10
# count = 0
# indexes = list(range(box))
# for _ in range(1000000):
#     nums = [0 for _ in range(box)]
#     for _ in range(ball):
#         index = random.choice(indexes)
#         nums[index] += 1
#     if Counter(nums).get(0) == 10:
#         count+=1
# print(count/1000000)


import random
total_number = 100000
def stimulation(balls = 10, boxes = [0] * 12):
    for i in range(balls):
        index = random.randint(0,11)
        boxes[index] += 1
    return boxes
def emptyBoxes(boxes):
    number = 0
    for item in boxes:
        if item == 0:
            number += 1
    return number
def simulations(number):
    ten_empty_boxes = 0
    for i in range(number):
        result = stimulation(10, [0] * 12)
        if emptyBoxes(result) == 10:
            ten_empty_boxes += 1
    return float(ten_empty_boxes) / total_number
print(simulations(total_number))