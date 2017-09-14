class Solution(object):
    def buildstr(self, seq):
        if len(seq)==1:
            return '1'+str(seq[0])
        i = 0
        l = len(seq)
        next = ''
        num = 1
        while i < l-1:
            if seq[i]==seq[i+1]: 
                i += 1
                num += 1
            else:
                next = next + str(num) + seq[i]
                num = 1
                i += 1
        next = next + str(num) + seq[i]
        return next
            
    def countAndSay(self, n):
        sequence = "1"
        i = 1
        while i < n:
            sequence = self.buildstr(sequence)
            i += 1
        return sequence

s = Solution()

print(s.countAndSay(6))

        
