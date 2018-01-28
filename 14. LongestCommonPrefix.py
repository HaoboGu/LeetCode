class Solution(object):
    def find_longest(self, s1, s2):
        """
        Find longest common prefix between string s1 and s2
        :param s1:
        :return:
        """
        min_l = min(len(s1), len(s2))
        l_common_prefix = 0
        for i in range(min_l):
            if s1[i] == s2[i]:
                l_common_prefix += 1
            else:
                break
        return s1[:l_common_prefix]


    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        else:
            lcp = strs[0]
        for i in range(1, len(strs)):
            lcp = self.find_longest(lcp, strs[i])
        return lcp
s = Solution()
print(s.longestCommonPrefix(['a', 'a', 'a']))