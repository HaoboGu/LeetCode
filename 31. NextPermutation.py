class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        leng = len(nums)
        if leng == 1:
            return
        flag = 0
        for i in range(leng-1, 0, -1):
            # for index from leng-1 to 1
            if nums[i] > nums[i-1]:
                # later number is greater than previous number
                j = leng - 1
                while nums[j] <= nums[i-1]:
                    j -= 1
                nums[j], nums[i-1] = nums[i-1], nums[j]  # swap
                nums[i:leng] = sorted(nums[i:leng])
                flag = 1
                break

        if flag == 0:
            nums.sort()
