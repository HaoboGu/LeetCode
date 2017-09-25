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
class Solution(object):
    def isSymmetric(self, root):
        # non-recursion version
        if not root or (not root.left and not root.right):
            return True            
        elif not root.left or not root.right:
            return False
        p = [root.left]
        q = [root.right]
        while p and q:
            # stack here
            val_p = p.pop()
            val_q = q.pop()
            if not val_p and not val_q:
                continue
            elif not val_p or not val_q:
                return False
            elif val_p.val == val_q.val:
                p.append(val_p.left)
                q.append(val_q.right)

                p.append(val_p.right)
                q.append(val_q.left)
            else:
                return False
        return True
            
