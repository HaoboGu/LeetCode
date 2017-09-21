class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            s = {}
            s[1] = 1
            s[2] = 2
            for i in range(3, n+1):
                s[i] = s[i-1] + s[i-2]
            return s[n]
s = Solution()
print(s.climbStairs(34))

