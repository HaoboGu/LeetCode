class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, smodify nums1 in-place instead.
        """
        l = len(nums1)-m
        for index in range(0, l):
            nums1.pop()
        num2 = nums2[0:n]
        for item in num2:
            if m == 0:
                nums1.insert(0, item)
                m += 1
                continue
            for index in range(0, m):
                if item < nums1[index]:
                    nums1.insert(index, item)
                    m += 1
                    break
                elif index == m-1:
                    nums1.insert(index+1, item)
                    m += 1



