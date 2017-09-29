import Queue
class Solution(object):
    def levelOrderBottom(self, root):
        if not root:
            return []
        q = Queue.Queue()
        depth = Queue.Queue()
        q.put(root)
        depth.put(1)
        result = []
        while not q.empty():
            node = q.get()
            current_dep = depth.get()
            if current_dep > len(result):
               result.append([node.val])
            else:
                result[current_dep-1].append(node.val)
            if node.left:
                q.put(node.left)
                depth.put(current_dep+1)
            if node.right:
                q.put(node.right)
                depth.put(current_dep+1)
        result.reverse()
        return result

import Queue
class Solution(object):
    def levelOrderBottom(self, root):
        if not root:
            return []
        q, depth, re= Queue.Queue(), Queue.Queue(), []
        q.put(root)
        depth.put(1)
        while not q.empty():
            node, current_dep = q.get(), depth.get()
            re.append([node.val]) if current_dep > len(re) else re[current_dep-1].append(node.val)
            [q.put(n) for n in (node.left, node.right) if n]
            [depth.put(current_dep+1) for n in (node.left, node.right) if n]
        return re[::-1]

