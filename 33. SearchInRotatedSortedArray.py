class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        left = 0
        right = len(nums) - 1
        return self.bi_search(nums, target, left, right)

    def bi_search(self, nums, target, left, right):
        # recursively search the target
        if right == left:  # base situation
            if nums[right] == target:
                return right
            else:
                return -1
        mid = left + (right - left) // 2  # left - mid, mid+1 - right
        if nums[left] > nums[mid]:
            # pivot is in the left half, the right half is in order
            if nums[right] >= target > nums[mid]:
                # print(mid, right)
                return self.bi_search(nums, target, mid + 1, right)
            else:
                return self.bi_search(nums, target, left, mid)
        else:
            # pivot is in the right half, the left half is in order
            if nums[mid] >= target >= nums[left]:
                return self.bi_search(nums, target, left, mid)
            else:
                return self.bi_search(nums, target, mid + 1, right)


s = Solution()
print(s.search([1,2,3], 2))