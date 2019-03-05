# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.recursion(root, None, None)

    def recursion(self, root, lower_limit, upper_limit):

        if lower_limit is not None and root.val <= lower_limit:
            return False
        if upper_limit is not None and root.val >= upper_limit:
            return False
        lf = True
        rf = True

        if root.left is not None:
            lf = self.recursion(root.left, lower_limit, root.val)
        if root.right is not None:
            rf = self.recursion(root.right, root.val, upper_limit)
        return lf and rf

