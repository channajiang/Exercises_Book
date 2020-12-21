# -*-coding:utf-8-*-

"""
一个有名的按摩师会收到源源不断的预约请求。每个预约都可以选择接或不接。在每次预约服务之间要
有休息时间，因此她不能接受相邻的预约。给定一个预约请求序列，替按摩师找到最优的预约集合
（最预约时间最长），返回总的分钟数

示例 1：

输入：nums = [1,2,3,1]
输出：4
解释：选择1号预约和3号预约，总时长 = 1 + 3 = 4

示例 2：

输入：nums = [2,7,9,3,1]
输出：12
解释：选择1号预约和3号和5号预约，总时长 = 2 + 9 + 1 = 12


示例 3：

输入：nums = [2,1,4,5,3,1,1,3]
输出：12
解释：选择1号, 3号,5号和 8号预约，总时长 = 2 + 4 + 3 + 3 = 12

动态规划
"""

from typing import List


class Solution:
    def msssage(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return n
        dp0, dp1 = 0, nums[0]
        for i in range(1, n):
            tdp0 = max(dp0, dp1)
            tdp1 = dp0 + nums[i]
            dp0, dp1 = tdp0, tdp1
        print(max(dp0, dp1))
        return max(dp0, dp1)


if __name__ == '__main__':
    nums = [2, 1, 4, 5, 3, 1, 1, 3]
    d = Solution()
    d.msssage(nums)
