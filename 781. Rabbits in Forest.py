import math
class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        if len(answers) <= 0:
            return 0
        dic = {}
        for i in answers:
            num = i + 1
            if num in dic:
                dic[num] = dic[num] + 1
            else:
                dic[num] = 1
        result = 0
        print(dic)
        for k, v in dic.items():
            count = math.ceil(v/k)
            result += count * k
        return int(result)


s = Solution()
print(s.numRabbits([0,0,1,1,1]))