class Solution(object):
    def addBinary(self, a, b):
        if not a:
            return b
        if not b:
            return a
        la, lb = len(a), len(b)
        i = 1
        s = ''
        carry = 0
        while i <= la or i <= lb:
            da = a[-i] if i <= la else '0'
            db = b[-i] if i <= lb else '0'
            if da  =='1' and db == '1':
                if carry == 0:
                    s = '0' + s
                else:
                    s = '1' + s
                carry = 1
            elif da == '0' and db == '0':
                if carry == 0:
                    s = '0' + s
                else:
                    s = '1' + s
                carry = 0
            elif carry == 1:
                s = '0' + s
            else:
                s = '1' + s
                carry = 0
            i += 1
        if carry == 1:
            s = '1' + s
        return s

s = Solution()
print(s.addBinary('111', '11'))

                

