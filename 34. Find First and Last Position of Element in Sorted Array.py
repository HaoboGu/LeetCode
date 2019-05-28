#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Problem 34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value
Your algorithm's runtime complexity must be in the order of O(log n)
If the target is not found in the array, return [-1, -1]
"""

__author__ = "Haobo Gu"
__email__ = "haobogu@outlook.com"
__date__ = "2019.05.17"


class Solution:
    def searchRange(self, nums, target: int):
        end = len(nums) - 1
        start = 0
        while start <= end:
            mid = start + (end - start + 1) // 2
            if nums[mid] == target:
                # expansion
                range_end = mid
                while range_end + 1 < len(nums) and nums[range_end + 1] == target:
                    range_end += 1
                range_start = mid
                while range_start - 1 >= 0 and nums[range_start - 1] == target:
                    range_start -= 1
                return [range_start, range_end]
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
            print(start, mid, end)

        return [-1, -1]

s = Solution()
print(s.searchRange([1,3], 1))