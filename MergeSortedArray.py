class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[:] = nums1[:m]
        nums2[:] = nums2[:n]
        cur_m, cur_n = 0, 0
        while cur_n < n and cur_m < m+n:
            if cur_m >= m + cur_n or nums1[cur_m] > nums2[cur_n]:
                nums1.insert(cur_m, nums2[cur_n])
                cur_n += 1
                cur_m += 1               
            elif nums1[cur_m] <= nums2[cur_n]:
                cur_m += 1
        nums1 = nums1[:m+n]            
        return nums1
s = Solution()
print(s.merge([1,2,3,6,7], 5, [5,6,8,12,43], 5))

'''
Note that there are spaces in the rear of nums1
So that starting from the biggest number is better
Just fill the blanks in the rear of nums1, rather than insert into nums1
'''

