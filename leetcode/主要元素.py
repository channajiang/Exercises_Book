# -*-coding:utf-8-*-


"""
数组中占比超过一半的元素称之为主要元素。给定一个整数数组，找到它的主要元素。
若没有，返回-1

示例 1：

输入：nums = [1,2,5,9,5,9,5,5,5]
输出：5

示例 2：

输入：nums = [3,2]
输出：-1

示例 3：

输入：nums = [2,2,1,1,1,2,2]
输出：2

说明：你有办法在时间复杂度为O(N),空间复杂度为O(1)内完成吗？


"""

from typing import List


class Solution(object):
    def majorityElement(self, nums: List[int]) -> int:
        if nums is None:
            return -1
        nums.sort()
        mid = len(nums) // 2
        if nums.count(nums[mid]) > len(nums) // 2:
            print(nums[mid])
            return nums[mid]
        else:
            print(-1)
            return -1

    def majorElement(self, nums: List[int]) -> int:
        count = 0
        mid = len(nums) // 2
        num = 0
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and i < j:
                    count += 1
                    num = nums[i]
                    break
        if count > mid:
            print(num)
            return num
        else:
            print(-1)
            return -1


if __name__ == '__main__':
    nums = [3, 2]
    d = Solution()
    d.majorElement(nums)
