#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Problem 95. Unique Binary Search Trees II

Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Solution:   Assume the root number is i, 1<=i<=n. Then, the left branch will be what's less than i, and right branch
            will be what's larger than i
"""

__author__ = "Haobo Gu"
__email__ = "haobogu@outlook.com"
__date__ = "2019.05.14"


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        """
        Generate trees
        :param n:
        :return:
        """
        if n == 0:
            return []
        return self.gen(1, n)

    def gen(self, start, end):
        """
        Different from prob 96, in this problem we need start and end to generate all trees, other than just count
        So we cannot use tmp to accelerate the algorithm
        :param start:   int
        :param end:     int
        :return:        List[RootNode]
        """
        if start > end:
            return [None]

        if start == end:
            return [TreeNode(start)]

        # start < end
        result = []
        for i in range(start, end + 1):
            left_trees = self.gen(start, i - 1)
            right_trees = self.gen(i + 1, end)
            for left_tree in left_trees:
                for right_tree in right_trees:
                    current_tree = TreeNode(i)
                    current_tree.right = right_tree
                    current_tree.left = left_tree
                    result.append(current_tree)
        return result




            
            