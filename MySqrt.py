class Solution(object):
    def mySqrt(self, x):
        left, right = 0, x
        while True:
            mid = (left + right)//2
            if mid*mid <= x < (mid+1)*(mid+1):
                return mid
            if mid * mid > x:
                right = mid
            else:
                left = mid + 1

a = Solution()
print(a.mySqrt(2))


