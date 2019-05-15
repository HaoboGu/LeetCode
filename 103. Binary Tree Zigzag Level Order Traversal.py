#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Problem 103. Binary Tree Zigzag Level Order Traversal

Given a binary tree, return the zigzag level order traversal of its nodes' values.
(ie, from left to right, then right to left for the next level and alternate between).

"""

__author__ = "Haobo Gu"
__email__ = "haobogu@outlook.com"
__date__ = "2019.05.15"


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        # if root is None:
        #     return []
        #
        # result = []
        # level_result = []
        # order = True
        # cur_level = [root]
        # next_level = []
        # while len(cur_level) > 0 or len(next_level) > 0:
        #     n = cur_level.pop(0)
        #     level_result.append(n.val)
        #     next_level += self.get_children_by_order(n, order)
        #     if len(cur_level) == 0:
        #         result.append(level_result)
        #         level_result = []
        #         cur_level = next_level[::-1]
        #         next_level = []
        #         order = not order
        #
        # return result

        # New
        if root is None:
            return []

        level = [root]
        result = []
        order = 1
        while level:
            result.append([n.val for n in level][::order])
            level = self.get_next_level(level)
            order *= -1

    def get_next_level(self, current_level):
        next_level = []
        for node in current_level:
            next_level += [child for child in (node.left, node.right) if child]
        return next_level

    def get_children_by_order(self, node, order):
        re = []
        if node.left is not None:
            re.append(node.left)
        if node.right is not None:
            re.append(node.right)
        return re if order else re[::-1]


