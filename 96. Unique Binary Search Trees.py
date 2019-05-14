#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Problem 96. Unique Binary Search Tree

Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Solution:   Assume the root number is i, 1<=i<=n. Then, the left branch will be what's less than i, and right branch
            will be what's larger than i
"""

__author__ = "Haobo Gu"
__email__ = "haobogu@outlook.com"

class Solution:
    def numTrees(self, n: int) -> int:

        tmp = {0: 1, 1: 1}
        return self.count(n, tmp)


    def count(self, n, tmp):
        """
        Recursively count.
        numTree(n) = numTree(i-1) + numTree(n-i) for i in 1~n
        :param n:
        :param tmp: store tmp results, avoid unnecessary computation
        :return:
        """

        if tmp.get(n):
            return tmp.get(n)
        else:
            num_tree = 0
            for i in range(1, n+1):
                num_tree += (self.count(i-1, tmp) * self.count(n-i, tmp))
        tmp[n] = num_tree
        return num_tree
