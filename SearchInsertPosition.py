class Solution(object):
    def searchInsert1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        l = len(nums)
        while nums[i] < target and i < l-1:
            i += 1
        if nums[i] < target:
            return l
        else:
            return i
    def searchInsert(self, nums, target):
        # binary search
        if target > nums[-1]:
            return len(nums)
        if target <= nums[0]:
            return 0
        head, tail = 0, len(nums) - 1
        i = (head + tail)//2
        while i > head:
            if nums[i]<target:
                head = i
            elif nums[i]>target:
                tail = i
            else:
                return i
            i = (head + tail)//2

        return head + 1
        
s = Solution()
print(s.searchInsert([1,2,6,8,9,10], 10))

