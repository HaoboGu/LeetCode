#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Problem 22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

"""

__author__ = "Haobo Gu"
__email__ = "haobogu@outlook.com"
__date__ = "2019.05.28"


class Solution:
    def generateParenthesis(self, n: int):
        return self.helper(2*n, n, n)

    def helper(self, length, left_to_add, right_to_add):
        result = []
        if length == 1 and right_to_add == 1:
            return [")"]

        if left_to_add > 0:
            result.extend(["(" + s for s in self.helper(length - 1, left_to_add - 1, right_to_add)])
        if left_to_add < right_to_add and right_to_add > 0:
            result.extend([")" + s for s in self.helper(length - 1, left_to_add, right_to_add - 1)])
        return result

s = Solution()
print(s.generateParenthesis(3))