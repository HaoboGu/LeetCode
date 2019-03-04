
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        max_reach = 0
        for i in range(0, len(nums) - 1):
            if i > max_reach:
                return False
            else:
                max_reach = max(max_reach, i + nums[i])
        return max_reach >= len(nums) - 1






s = Solution()
print(s.canJump([4,1,2,3,3,0,0,1]))