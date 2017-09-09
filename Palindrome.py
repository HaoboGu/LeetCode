class Solution(object):
    def isPalindrome(self, x):
        if x < 0 and abs(x)<:
            return False
        reverse = 0
        t = x
        while x:
            reverse = reverse*10 + x%10
            x = (x-x%10)/10
        if reverse == t:
            return True
        else:   
            return False
s = Solution()
print(s.isPalindrome(122321))

