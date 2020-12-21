# -*-coding:utf-8-*-


"""
给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)

示例 1：

输入：nums = [3,2,1]
输出：1

示例 2：

输入：nums = [1,2]
输出：2
解释：第三大的数不存在，所以返回最大的数2

示例 3：

输入：nums = [2,2,3,1]
输出：1
解释：注意，要求返回第三大的数，是指第三大且唯一出现的数
存在两个值为2的数，它们都排第二


"""

from typing import List


class Solution(object):
    def thirdMax(self, nums: List[int]) -> int:
        set_nums = set(nums)
        if len(set_nums) < 3:
            return max(set_nums)
        else:
            set_nums.remove(max(set_nums))
            set_nums.remove(max(set_nums))
            print(max(set_nums))
            return max(set_nums)

if __name__ == '__main__':
    nums = [2, 2, 3, 1]
    d = Solution()
    d.thirdMax(nums)