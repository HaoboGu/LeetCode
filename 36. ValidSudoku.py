import numpy as np

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        b = np.array(board)
        for ele in b:
            for i in range(1, 10):
                if np.count_nonzero((ele == str(i))) > 1:
                    return False

        for ele in b.transpose():
            for i in range(1, 10):
                if np.count_nonzero((ele == str(i))) > 1:
                    return False

        for i in range(0, 3):
            for j in range(0, 3):
                rows = [3 * i, 3*i + 1, 3 * i + 2]
                cols = [3 * j, 3*j + 1, 3 * j + 2]
                sub_matrix = b[np.ix_(rows, cols)]
                for number in range(1, 10):
                    if np.count_nonzero(sub_matrix == str(number)) > 1:
                        return False
        return True

s = Solution()
print(s.isValidSudoku([[".",".","4",".",".",".","6","3","."],[".",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".","9","."],[".",".",".","5","6",".",".",".","."],["4",".","3",".",".",".",".",".","1"],[".",".",".","7",".",".",".",".","."],[".",".",".","5",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]))
