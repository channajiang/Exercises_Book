"""
设计一个算法，算出n阶乘有多少个尾随零

示例 1：

输入：3
输出：0
解释： 3！ = 6，尾数中没有0


示例 2：
输入：5
输出：1
解释： 5！ = 120，尾数中有1个0
"""

class Solution:
    def fact(self, n):
        if n == 1:
            return 1
        return n * self.fact(n - 1)


    def trailngZeroes(self, n:int)-> int:
        res = 0
        while n > 0:
            n = n//5
            res += n
        print(res)
        return res

if __name__ == '__main__':
    n = 25
    d = Solution()
    # result = d.fact(n)
    # print(result)
    d.trailngZeroes(n)

