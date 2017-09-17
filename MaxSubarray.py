class Solution(object):
    def maxSubArray(self, nums):
        l = len(nums)
        maxSum = nums[0]
        currentSum = nums[0]
        for i in range(1, l):
            currentSum = max(currentSum + nums[i], nums[i])
            maxSum = max(maxSum, currentSum)
        return maxSum

s = Solution()
print(s.maxSubArray([2,-5,1,4,6,-4,5,-7,3,-4,-5,6,3,-2,6]))

