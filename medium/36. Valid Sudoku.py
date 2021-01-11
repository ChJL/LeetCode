'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
'''
# This solution is from leetcode
'''
Note: use list of dictionary. each row, col, square is corresponded to a dictionary
Such dict record the numbers' times of appearance. 
Therefore, if a number hav the value more than 1, it means duplicate --> false

The rules of index for square(box) is also useful in this solution.
'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [{} for i in range (9)]
        col = [{} for i in range(9)]
        square = [{} for i in range(9)]
        print(row)
        for i in range(9):
            for j in range(9):
                ele = board[i][j]

                if ele != ".":
                    sq_index = (i//3)*3 + j//3
                    # // is floor devision

                    row[i][ele] = row[i].get(ele,0) +1
                    col[j][ele] = col[j].get(ele,0) +1
                    square[sq_index][ele] = square[sq_index].get(ele, 0) +1

                    if row[i][ele]>1 or col[j][ele]>1 or square[sq_index][ele]>1:
                        return 0
        print(row)
        return 1
        
        
                