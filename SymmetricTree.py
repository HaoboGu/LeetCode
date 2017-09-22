class Solution(object):
    def isSymmetric(self, root):
        def t(l, r):
            if l and r and l.val == r.val:
                return t(l.right, r.left) and t(l.left, r.right)
            else:
                return l==r
        if not root:
            return True
        elif root.left and root.right and root.left.val == root.right.val:
            return t(root.left, root.right) 
        else: 
            return root.left == root.right

