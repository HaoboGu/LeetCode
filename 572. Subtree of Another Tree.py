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


    def assertTree(self, s, t):
        if s == None and t == None:
            return True
        if s != None and t!= None:
            if s.val == t.val:
                return self.assertTree(s.left, t.left) and self.assertTree(s.right, t.right)
        return False
