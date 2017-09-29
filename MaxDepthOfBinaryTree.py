class Solution(object):
    def maxDepth(self, root):
        # recursion version
        if not root:
            return 0
        if not root.right and not root.left:
            return 1
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1
class Solution(object):
    def maxDepth(self, root):
        # DFS (with stack)
        if not root:
            return 0
        st = []
        depths = []
        depth = 0
        st.append(root)
        depths.append(1)
        while st:
            node = st.pop()
            current_depth = depths.pop()
            if current_depth > depth:
                depth = current_depth
            if node.left:
                st.append(node.left)
                depths.append(current_depth+1)
            if node.right:
                st.append(node.right)
                depths.append(current_depth+1)
        return depth
import Queue
class Solution(object):
    def maxDepth(self, root):
        # BFS (queue)
        if not root:
            return 0
        q = Queue.Queue()
        q.put(root)
        depth = Queue.Queue()
        depth.put(1)
        max_depth = 0
        while not q.empty():
            node = q.get()
            current_depth = depth.get()
            if current_depth > max_depth:
                max_depth = current_depth
            if node.left:
                q.put(node.left)
                depth.put(current_depth+1)
            if node.right:
                q.put(node.right)
                depth.put(current_depth+1)
        return max_depth
