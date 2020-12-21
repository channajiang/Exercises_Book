# -*-coding:utf-8-*-


"""
给定一个整数数组，找出总和最大的连续数列，并返回总和
示例 1：

输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组[4,-1,2,1]的和最大

动态规划
nums[i] = max(nums[i-1], nums[i])
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return n
        # 初始化sum, max_sum
        sum, max_sum = float('-inf'), float('-inf')
        # 对于每个nums[i]：
        for i in nums:
            # sum = max(nums[i-1], nums[i])
            sum = max(sum + i, i)
            max_sum = max(sum, max_sum)
        print(max_sum)
        return max_sum


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    d = Solution()
    d.maxSubArray(nums)
