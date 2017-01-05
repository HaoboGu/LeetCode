class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        l = []
        for i in range(1, n + 1):
            l.append(self.isFZ(i))
        return l

    def isFZ(self, n):

        if n % 15 == 0:
            return "FizzBuzz"
        elif n % 3 == 0:
            return 'Fizz'
        elif n % 5 == 0:
            return 'Buzz'
        else:
            return str(n)



s  =Solution()
ls = s.fizzBuzz(15)
print(ls)