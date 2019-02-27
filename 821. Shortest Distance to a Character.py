class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        distance = [0] * len(S)
        pos = self.find_all(S, C)
        for i in range(0, len(pos)):
            curPos = pos[i]
            if i == 0:
                for j in range(0, curPos):
                    distance[j] = curPos - j
            if i + 1 == len(pos):
                for j in range(curPos+1, len(S)):
                    distance[j] = j - curPos
            else:
                nextPos = pos[i + 1]
                for j in range(curPos+1, nextPos):
                    distance[j] = min(j - curPos, nextPos - j)

        return distance




    def find_all(self, S, C):
        start = 0
        result = []
        pos = S.find(C, start)
        while pos != -1:
            result.append(pos)
            start = pos + 1
            pos = S.find(C, start)
        return result

