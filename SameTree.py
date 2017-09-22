class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        elif not p or not q:
            return False
        
        if q.val == p.val and self.isSameTree(q.right, p.right) and self.isSameTree(q.left, p.left):
            return True
        else:
            return False

