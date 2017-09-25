class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        if not root.right and not root.left:
            return 1
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1
