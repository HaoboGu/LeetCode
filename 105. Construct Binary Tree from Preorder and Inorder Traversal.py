# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder is None:
            return

        return self.helper(0, 0, len(inorder)-1, preorder, inorder)


    def helper(self, pre_index, in_index_start, in_index_end, preorder, inorder):

        if pre_index >= len(preorder) or in_index_start > in_index_end:
            return None
        root = preorder[pre_index]
        root_node = TreeNode(root)
        in_index = 0
        # Get current root in inorder array
        for i in range(in_index_start, in_index_end+1):
            if inorder[i] == root:
                in_index = i
                break


        root_node.left = self.helper(pre_index + 1, in_index_start, in_index-1, preorder, inorder)
        root_node.right = self.helper(pre_index + 1 + in_index - in_index_start, in_index+1, in_index_end, preorder, inorder)

        return root_node