"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
"""

# 一次可以跳上1级台阶, n级的台阶
# 一次可以跳上2级台阶, n级的台阶
# 混着跳

# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 1 or number == 0:
            return number
        a = 1
        b = 1
        i = 2
        while i <= number:
            i += 1
            a = a + b
            b = a - b
        print(a)
        return a

if __name__ == '__main__':
    d = Solution()
    d.jumpFloor(9)