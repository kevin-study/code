"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
示例 1:
输入: 123
输出: 321
示例 2:
输入: -123
输出: -321
示例 3:
输入: 120
输出: 21
注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
"""


class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            y = str(x).split('-')[1]
        else:
            y = str(x)
        y = y[::-1]
        if x < 0:
            re = int('-' + y)
        else:
            re = int(y)
        if re < -2 ** 31 or re > 2 ** 31 - 1:
            return 0
        return re


s = Solution()
print(s.reverse(1534236469))
