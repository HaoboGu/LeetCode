class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return self.method1(nums, target)

    def method1(self, nums, target):
        """
        Two pointers
        :param nums:
        :param target:
        :return:
        """
        if len(nums) < 4:
            return []
        nums = sorted(nums)
        results = []
        i = 0
        while i < len(nums) - 3:
            j = i + 1
            while j < len(nums) - 2:
                head = j + 1
                tail = len(nums) - 1
                while head < tail:
                    if nums[i] + nums[j] + nums[head] + nums[tail] == target:
                        results.append([nums[i], nums[j], nums[head], nums[tail]])
                        head += 1
                        while nums[head - 1] == nums[head] and head < tail:
                            head += 1
                    elif nums[i] + nums[j] + nums[head] + nums[tail] < target:
                        head += 1
                        while nums[head - 1] == nums[head] and head < tail:
                            head += 1
                    elif nums[i] + nums[j] + nums[head] + nums[tail] > target:
                        tail -= 1
                        while nums[tail + 1] == nums[tail] and tail > head:
                            tail -= 1
                j += 1
                while nums[j] == nums[j-1] and j < len(nums) - 2:
                    j += 1
            i += 1
            while nums[i] == nums[i-1] and i < len(nums) - 3:
                i += 1
        return results


s = Solution()
print(s.fourSum([-3,-2,-1,0,0,1,2,3], 0))