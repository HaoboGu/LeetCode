class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dig_letter = {'1':[''], '2':['a', 'b', 'c'], '3':['d', 'e', 'f'], '4':['g', 'h', 'i'], '5':['j', 'k', 'l'],
                      '6': ['m', 'n', 'o'], '7':['p', 'q', 'r', 's'], '8':['t', 'u', 'v'], '9':['w', 'x', 'y', 'z'],
                      '0':[' ']}
        result_set = []
        for i in range(len(digits)):
            if len(result_set) == 0:
                for item in dig_letter[digits[i]]:
                    result_set.append(item)
            else:
                new_result_set = []
                for item in dig_letter[digits[i]]:
                    for pre_re in result_set:
                        # print(pre_re, item)
                        new_re = pre_re+item
                        new_result_set.append(new_re)
                result_set = new_result_set
        # print(result_set)
        return result_set


s = Solution()
s.letterCombinations('23')