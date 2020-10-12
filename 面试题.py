"""
- （必答）部⻔优化
某公司内有 4 个项⽬组，项⽬组 A、B、C、D，项⽬组A现有10⼈，项⽬组B现有7⼈，项⽬组C现
有5⼈，项⽬组D现有4⼈。为了实现跨项⽬组协作，公司决定每⽉从⼈数最多的项⽬组中抽调 3 ⼈
出来，到其他剩下 3 组中，每组 1 ⼈，这称之为⼀次调整优化（亦即经过第⼀次调整后，A组有7
⼈，B组有8⼈，C组有6⼈，D组有5⼈）。
那么请问，经过⼗年的优化调整后，各项⽬组各有⼏⼈？
编程求解该问题，并思考是否为最优解。
"""

# def department_optimize(dep, year):
#     month = year * 12
#     for i in range(month):
#         maxNum = max(dep.values())
#         for item in dep:
#             if dep[item] == maxNum:
#                 dep[item] -= 3
#             else:
#                 dep[item] += 1
#     return dep
#
#
# dept = {
#     'A': 10,
#     'B': 7,
#     'C': 5,
#     'D': 4
# }
# y = 10
# print(department_optimize(dept, y))
from time import time

"""
- （必答）邀请码检测
某产品的⽤户注册邀请码为⼀串有⼩写字⺟和数字组成的字符串，字符串⻓度为16。当⽤户数据邀
请码的时候，系统需要对邀请码做有效性验证，假设验证规则如下：
1、 从序列号最后⼀位字符开始，逆向将奇数位(1、3、5等等)相加；
2、从序列号最后⼀位数字开始，逆向将偶数位数字，先乘以2（如果乘积为两位数，则将其减去
9），再求和；
3、将奇数位总和加上偶数位总和，结果可以被10整除；
4、⼩写字⺟对应数值，可由下⾯键值对确定；
[(a,1), (b,2), (c,3)…,(i,9), (j,1), (k, 2)…]，亦即，按字⺟顺序，1-9循环。
输⼊：输⼊16位字符串，表示邀请码
输出：输出“ok”或者“error”
"""

# def invitation_code(code):
#     odd_num = 0
#     for i in range(-1, -len(code) - 1, -2):
#         if ord(code[i]) > 10:
#             for o in letter:
#                 if o[0] == code[i]:
#                     num = o[1]
#                     odd_num += num
#         else:
#             odd_num += ord(code[i])
#     even_num = 0
#     for i in range(-2, -len(code) - 1, -2):
#
#         if ord(code[i]) > 10:
#             for e in letter:
#                 if e[0] == code[i]:
#                     num = e[1] * 2 if e[1] * 2 < 10 else e[1] * 2 - 9
#         else:
#             num = ord(code[i]) if ord(code[i]) * 2 < 10 else ord(code[i]) * 2 - 9
#         even_num += num
#     if (odd_num + even_num) % 10 != 0:
#         return 'error'
#     else:
#         return 'ok'
#
#
# letter = [("a", 1), ("b", 2), ("c", 3), ("d", 4), ("e", 4), ("f", 6), ("g", 7), ("h", 8), ("i", 9), ("j", 1), ("k", 2),
#           ("l", 3), ("m", 4), ("n", 5), ("o", 6), ("p", 7), ("q", 8), ("r", 9), ("s", 1), ("t", 2), ("u", 3), ("v", 4),
#           ("w", 5), ("x", 6), ("y", 7), ("z", 8)]
# # print(len(letter))
# aa = 'aaaabbb111223456'
# print(invitation_code(aa))
"""
- （必答）游戏币组合
⼩明的抽屉⾥有n个游戏币，总⾯值m，游戏币的设置有1分的，2分的，5分的，10分的，⽽在⼩明
所拥有的游戏币中有些⾯值的游戏币可能没有，求⼀共有多少种可能的游戏币组合⽅式？
输⼊：输⼊两个数n(游戏币的个数)，m(总⾯值)。
输出：请输出可能的组合⽅式数；
"""


#
def combine_coin(n, m):
    uu = 0
    re = []
    if n < m and m < 10 * n:
        for i in range(n+1):
            for k in range(n-i+1):
                for r in range(n-i-k+1):
                    for u in range(n-i-k-r+1):
                        print(uu)
                        uu+=1
                        if i * 10 + k * 5 + r * 2 + u == m and i + k + r + u == n:
                            re.append((i, k, r, u))
    elif n == m:
        return {'1': m}
    elif m == 10 * n:
        return {'10': n}
    return re


a = combine_coin(5002, 10000)
print(a)
"""
有数学家发现⼀些两位数很有意思，⽐如，
34 * 86 = 43 * 68
也就是说，如果把他们的⼗位数和个位数交换，⼆者乘积不变。
编程求出满⾜该性质的两位数组合。
提示，暴⼒解法⾮最优解。
"""

# def solution():
#     list1 = []
#     for i in range(11, 100):
#         for k in range(11, 100):
#             if i * k == ((i % 10) * 10 + i // 10) * ((k % 10) * 10 + k // 10):
#                 list1.append((i, k))
#     return list1
#
#
# t1 = time()
# print('t1:', t1)
# print(solution())
# t2 = time()
# print(t2 - t1)
