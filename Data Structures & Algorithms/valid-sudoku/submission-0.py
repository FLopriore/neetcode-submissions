class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        freq_column = [[0] * 9 for _ in range(9)]
        freq_block = [[0] * 9 for _ in range(9)]
        for i in range(9):
            freq_row = [0]*9
            for j in range(9):
                value = board[i][j]
                if value != '.':
                    idx_value = int(value)-1
                    freq_row[idx_value] += 1
                    if freq_row[idx_value] > 1:
                        return False
                    
                    freq_column[j][idx_value] += 1
                    if freq_column[j][idx_value] > 1:
                        return False
                    
                    freq_block[(j // 3) + 3 * (i // 3)][idx_value] += 1
                    if freq_block[(j // 3) + 3 * (i // 3)][idx_value] > 1:
                        return False
        return True