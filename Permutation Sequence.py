import math
class Solution(object):
    result = []
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        list = []
        i = n
        for x in range(0, n):
            list.append(x + 1)
        if k == 1:
            re = "".join(str(i) for i in list)
            return re
        for x in range(0, n):
            num = math.factorial(i-1)
            if k % num == 0:
                di = k // num
            else:
                di = k // num + 1
            self.result.append(list[di-1])
            list.remove(list[di-1])
            k = k - (di-1) * num
            i -= 1

        re = "".join(str(i) for i in self.result)
        print(re)

        return re
    



