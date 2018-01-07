def isP(s):
    l = len(s) - 1
    for i in range(0, len(s)//2):
        if s[i] != s[l-i]:
            return False
    return True


class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        # 1. Brute Force
        # l = len(s)
        # start = 0
        # end = start
        # max_l = 0
        # re = ''
        # while start < l and l - start > max_l:
        #     end = start
        #     while end < l:
        #         if isP(s[start:end+1]):
        #             if end-start+1 > max_l:
        #                 max_l = end-start+1
        #                 re = s[start:end+1]
        #         end += 1
        #     start += 1
        # print(re)

        # 2. expand from center
        # there are 2n-1 centers

        # (1) single character center
        # max_l = 0
        # re = ''
        # center_end = center_start = 0
        # while center_end < len(s):
        #     cur_l = 0 if center_end != center_start else -1  # +2 in the following step
        #     shift = 0
        #     while center_start - shift >= 0 and center_end + shift < len(s):
        #         if s[center_start-shift] == s[center_end+shift]:
        #             cur_l += 2
        #             shift += 1
        #         else:
        #             break
        #     if cur_l > max_l:
        #         max_l = cur_l
        #         re = s[center_start-shift+1:center_end+shift]
        #     if center_end != center_start:
        #         center_start = center_end
        #     else:
        #         center_end += 1
        # # print(re)
        # return re

        # 3. optimized method
        # From left to right, every time we increase by 1 character, the length longest Palindrome can increase at most
        # 2. That is, we only need to verify the substring ends with the new character and whose length is max+1 or
        # max+2.
        # When we increase by 1 character, the length of longest Palindrome cannot increase 3 because if that, we can
        # drop the last and the first characters of that substring and the rest is also a Palindrome, whose length is
        # max+1, which is contradict with previous assumption
        # cur_pos = 0
        max_l = 0
        re = ''
        for i in range(0, len(s)):
            if i-max_l-1 >= 0:
                if isP(s[i-max_l-1:i + 1]):
                    re = s[i - max_l - 1:i + 1]
                    max_l += 2
                    continue
            if i - max_l >= 0:
                if isP(s[i-max_l:i+1]):
                    re = s[i - max_l:i + 1]
                    max_l += 1

        return re


s = Solution()
s.longestPalindrome('asdasddsadasd')