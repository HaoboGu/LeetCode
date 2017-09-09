class Solution(object):
    def isValid(self, s):
        Left = {'(':')', '[':']', '{':'}'}
        l = []
        num = 0
        for i in s: 
            if i in Left:
                l.append(i)
            else:
                if len(l)<=0:
                    return False
                elif Left[l[len(l)-1]]==i:
                    l.pop(len(l)-1)
                else:
                    return False

        if len(l)!=0:
            return False
        else:
            return True

s = Solution()
print(s.isValid("()(([])){}{}[][]"))

