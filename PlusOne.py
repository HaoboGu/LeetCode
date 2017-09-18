class Solution(object):
    def plusOne(self, digits):
        decent = 1
        for i in range(1, len(digits)+1):
            s = decent + digits[-i]
            if s >= 10:
                digits[-i] = s % 10
                decent = 1
            else:
                digits[-i] = s
                decent = 0
                break
        if decent == 1:
            digits = [1] + digits
        return digits
