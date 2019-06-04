#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Problem 46. Permutations


"""

__author__ = "Haobo Gu"
__email__ = "haobogu@outlook.com"
__date__ = "2019.06.04"


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]

        result = []
        for i in range(0, len(nums)):
            cur_num = nums[i]
            new_nums = nums[:i] + nums[i+1:]
            sub_re = self.permute(new_nums)
            if len(sub_re) >= 1:
                for sub_num in sub_re:
                    result.append([cur_num] + sub_num)

        return result
