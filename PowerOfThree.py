class Solution(object):

    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        elif n == 1:
            return True
        else:
            return self.isPowerOfThree(n/3)

s = Solution()
print(s.isPowerOfThree(81))
