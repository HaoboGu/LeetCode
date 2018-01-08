
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # d1 = create_new_list(nums)
        # re = []
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]+nums[j] in d1 and i!=d1[nums[i]+nums[j]] and j!=d1[nums[i]+nums[j]]:
        #             # print(nums[i], nums[j])
        #             if sorted([nums[i], nums[j], -(nums[i]+nums[j])]) not in re:
        #                 re.append(sorted([nums[i], nums[j], -(nums[i]+nums[j])]))


        # n^2 method
        re = []
        s = sorted(nums)
        for i in range(len(s)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i+1
            r = len(s)-1
            while l < r:
                if s[i] + s[l] + s[r] > 0:
                    r -= 1
                elif s[i] + s[l] + s[r] < 0:
                    l += 1
                else:
                    re.append([s[i], s[l], s[r]])
                    while l < r and s[l] == s[l+1]:
                        l += 1
                    while l < r and s[r] == s[r-1]:
                        r -= 1
                    l += 1
                    r -= 1

        # print(re)
        return re

s = Solution()
s.threeSum([-1,0,1,2,-1,-4])
