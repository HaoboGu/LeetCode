class Solution(object):
    def func(self, x):
        return {
            '{': '}',
            '(': ')',
            '[': ']',
            }[x]

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for index in range(0, len(s)):
            if s[index] == '(' or s[index] == '{' or s[index] == '[':
                stack.append(s[index])
            elif s[index] == ')' or s[index] == '}' or s[index] == ']':
                if len(stack) == 0:
                    return False
                else:
                    chara = stack.pop()
                    if self.func(chara) != s[index]:
                        return False
        if len(stack) == 0:
            return True
        else:
            return False

so = Solution()

print(so.isValid('asd((as[](])as)'))
