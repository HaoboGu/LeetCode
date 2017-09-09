class Solution(object):
    def romanToInt(self, s):
        RomanSpDict={"IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}
        RomanDict={"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        i=0
        num=0
        while i+1<len(s):           
            if (s[i]+s[i+1]) in RomanSpDict:
                num = num + RomanSpDict[s[i]+s[i+1]]
                i+=2
            else:
                num = num + RomanDict[s[i]]
                i+=1
        if i != len(s):
            num += RomanDict[s[i]]
        return num

s = Solution()
print(s.romanToInt("MCMXC"))

" A smarter solution: 
    If a letter less than its latter one, we should subtract this.
    Example: IV, I<V, so we should -1 then +5. 
    The loop should look like this:
        for i in range(len(s)-1):
            if RomanDict[i]<RomanDict[i+1]:
                num -= RomanDict[i]
            else:
                num += RomanDict[i]   
        num += RomanDict[len(s)-1] # the last letter should always be added

"
