class Solution(object):
    def singleNumber(self, nums):
        """
        Given an array of integers, every element appears three times except for one. Find that single one.
        """

        """
        One Line Solution:
        Use set(), set() can get a set(without same number).
        For example: list = [1,2,1,3,4], set(list) = [1,2,3,4]

        code:
        return (3*sum(list(set(A)))-sum(A))/2
        """
        """
        Another solution: Bit operation
        When the order of bit operation is changed, the result remains unchanged.
        3 states: 00 -> 01 -> 10 -> 00
        frequency:0  -> 1  -> 2  -> 3(0)
        Use two bits to store every bit of the number
        XOR(^):same->0, else->1
        """

        ones = 0
        twos = 0
        for item in nums:
            # If bit2 == 0, just XOR(00>01); if bit2 == 1, >00
            ones = (ones ^ item) & (~twos)
            # If bit1 == 1，说明刚运算过,应为01, bit2=0; If bit1 == 0, 说明已XOR两次，所以bit2=1
            twos = (twos ^ item) & (~ones)
        return twos | ones


