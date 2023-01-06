class Solution:
    def isValidSudoku(self, board):
        seen = []
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c != '.':
                    seen.append((c,i))
                    seen.append((j,c))
                    seen.append((i//3, c, j//3))
        return len(seen) == len(set(seen))
