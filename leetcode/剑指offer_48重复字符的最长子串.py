# -*- coding: UTF-8 -*-

"""
请从字符串中找出一个最长的不包含重复字条的子字条串，计算该最长字符串的长度
example 1:
输入：‘abcabcbb’
输出：3
解释：因为无重复字符的最长子串是‘abc',所以其长度为3

example 2:
输入：‘bbbbb’
输出：1
解释：因为无重复字符的最长子串是‘b',所以其长度为1


example 3:
输入：‘pwwkew’
输出：1
解释：因为无重复字符的最长子串是‘wke',所以其长度为1

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Set = set()
        left, right, longest = 0, 0, 0
        while right < len(s):
            while s[right] in Set:
                Set.remove(s[left])
                left += 1
            Set.add(s[right])
            right += 1
            longest = max(right - left, longest)
        print(longest)
        return longest


if __name__ == '__main__':
    s = "pwwkew"
    a = Solution()
    a.lengthOfLongestSubstring(s)