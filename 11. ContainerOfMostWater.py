class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0
        end = len(height) - 1
        m_area = 0

        while start < end:
            if height[end] > height[start]:
                cur_a = (end-start) * height[start]
                start += 1
            else:
                cur_a = (end - start) * height[end]
                end -= 1
            m_area = max(cur_a, m_area)



        return m_area