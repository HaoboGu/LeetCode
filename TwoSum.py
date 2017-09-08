class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(0, len(nums)):
            if nums[i] not in dict:
                dict[target-nums[i]]=i
            else:
                return [i, dict[nums[i]]]

s = Solution()
print(s.twoSum([1,2,3,4,5,6,7,8,9], 17))

