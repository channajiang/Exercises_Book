# -*- coding: UTF-8 -*-
"""
判断一个整数是否是回文数，回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数
示例:
输入：121
输出：true
"""

# from pip._vendor.distlib.compat import raw_input
#
# s = int(raw_input("请输入一个数:\n"))
# a = s // 10000
# # b = s % 10000 // 1000
# # c = s % 1000 // 100
# # d = s % 100 // 10
# # e = s % 10
#
# if a == e and b == d:
#     print('%d 是回文数' %s)
# else:
#     print('%d 并不是回文数' %s)

# 小于0的数和能被10整除且不为0的数，一定不是回文数
# 新建变量rem，用于保存由x计算的倒序数
# 循环，当x>rem, 取下x的最后一位，并添加到rem上。此过程是利用数学公式，整除和求余
# 循环结束后的判断条件： 当 x == rem 或 x == rem//10,则是回文数；否则不是回文数

class Solution:
    def isPalindrome(self, x:int) -> bool:
        if x < 0 or (x % 10 == 0 and x !=0):
            print("不是回文数")
            return False
        rem = 0
        while x > rem:
            a = x % 10
            print(a)
            rem = rem * 10 + x % 10
            x = x // 10
        if x == rem or x == rem // 10:
            print("输入的是回文数")
            return x == rem or x == rem // 10
        else:
            print("输入的不是回文数")

if __name__ == '__main__':
    x = 6996
    b = Solution()
    b.isPalindrome(x)