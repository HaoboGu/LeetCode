class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        if nums==[]:
            return []
        while i+1 < len(nums):
            if nums[i] == nums[i+1]:
                nums.pop(i+1)
            else:
                i+=1
        return nums

s = Solution()
a = s.removeDuplicates([])
print(a)

