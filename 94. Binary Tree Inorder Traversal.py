# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        result = []
        stack = [root]
        current = root
        while len(stack) > 0:
            if current is None:
                break
            elif current.left is None:
                result.append(stack.pop())
                if current.right is not None:
                    stack.append(current.right)
                    current = current.right
                else:
                    current = 
            else:
                # left is not None
                current = current.left


        return result


