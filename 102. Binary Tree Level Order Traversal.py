# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def levelOrder(self, root: TreeNode) -> List[List[int]]:
    #     if root is None or root.val is None:
    #         return []
    #
    #     q = [root]
    #     result = [[root.val]]
    #     next_level = []
    #     while q.__len__() > 0:
    #         # queue is not empty
    #         current_node = q.pop(0)
    #         if current_node.left is not None:
    #             next_level.append(current_node.left)
    #         if current_node.right is not None:
    #             next_level.append(current_node.right)
    #         if q.__len__() == 0:
    #             if next_level.__len__() == 0:
    #                 break
    #             else:
    #                 result.append(self.nodes2values(next_level))
    #                 q = next_level
    #                 next_level = []
    #     return result

    def nodes2values(self, node_list):
        return [node.val for node in node_list]

    def helper(self, level):
        """
        :param level: level
        :return:   next_level
        """
        if level is None or len(level) == 0:
            return None, None
        next_level = []
        for node in level:
            if node.left is not None:
                next_level.append(node.left)
            if node.right is not None:
                next_level.append(node.right)
        return next_level, [n.val for n in level]

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None or root.val is None:
            return []
        level = [root]
        result = []
        level, val_list = self.helper(level)
        while level is not None:
            if val_list is not None:
                result.append(val_list)
            level, val_list = self.helper(level)
        return result



