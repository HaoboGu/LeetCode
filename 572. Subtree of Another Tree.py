# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        q = []
        if s != None:
            q.append(s)

        while len(q) > 0:
            cur = q.pop()
            if cur.right != None:
                q.append(cur.right)
            if cur.left != None:
                q.append(cur.left)
            if self.assertTree(cur, t):
                return True
        return False

    def isSame(self, s, t):
        if s == None and t == None:
            return True
        if s == None or t == None or s.val != t.val:
            return False

        return self.isSame(s.left, t.left) and self.isSame(s.right, t.right)

