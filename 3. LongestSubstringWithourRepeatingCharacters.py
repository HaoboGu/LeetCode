class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s.__len__() <= 1:
            return s.__len__()
        char_dict = {}
        cur_max = 0
        str_start = 0
        for index in range(0, len(s)):
            if s[index] in char_dict and char_dict[s[index]] >= str_start:
                cur_max = index - str_start if index - str_start > cur_max else cur_max
                str_start = char_dict[s[index]] + 1
            char_dict[s[index]] = index

        if s.__len__() - str_start > cur_max:
            cur_max = s.__len__() - str_start
        return cur_max

s = Solution()
print(s.lengthOfLongestSubstring('cdd'))