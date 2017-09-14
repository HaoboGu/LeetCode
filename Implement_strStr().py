class Solution(object):

    # Brute force method

    # def strStr(self, haystack, needle):
    #     if not needle:
    #         return -1
    #     l = len(needle)
    #     j = 0
    #     for i in range(0, len(haystack)-l+1):
    #         while haystack[i+j] == needle[j]:
    #             if j == l-1:
    #                 return i
    #             j += 1
    #         j=0
    #     return -1

    # KMP algorithm
    def partial(self, word):
        if len(word) == 1:
            table = [-1]
        elif len(word) == 2:
            table = [-1, 0]
        else:
            table = [None for i in range(len(word))]
            table[0] = -1
            table[1] = 0
            value = 0
            i = 2
            while i < len(word):
                if word[i - 1] == word[value]:
                    value += 1
                    table[i] = value
                    i += 1
                elif value > 0:
                    value = table[value]
                else:
                    table[i] = 0
                    i += 1
        return table

    def build_kmp_table(self, word):
        if len(word) == 1:
            table = [-1]
        elif len(word) == 2:
            table = [-1, 0]
        else:
            table = [None for i in range(len(word))]
            table[0] = -1
            table[1] = 0
            value = 0
            for i in range(2, len(word)):
                while word[i-1] != word[value] and value >= 0:
                    value = table[value]
                if value < 0:
                    table[i] = 0
                    value = 0
                else:
                    value += 1
                    table[i] = value
        return table


    def strStr(self, haystack, needle):
        if needle == '':
            return 0
        j = 0
        i = 0
        hl = len(haystack)
        nl = len(needle)
        next = self.partial(needle)
        while i < hl and j < nl:
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = next[j]
        if j == nl:
            return i - j
        return -1

s = Solution()
st = 'abcdabe'
# print(s.build_kmp_table(st))
# print(partial(st))
stt = 'db'
print(s.strStr(st, stt))
