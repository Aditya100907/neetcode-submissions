class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    # check rows
        for row in board:
            digits = [x for x in row if x != "."]
            if len(digits) != len(set(digits)):
                return False
        
        # check columns
        for col in range(9):
            digits = [board[row][col] for row in range(9) if board[row][col] != "."]
            if len(digits) != len(set(digits)):
                return False
        
        # check 3x3 boxes
        for boxr in range(3):
            for boxc in range(3):
                digits = []
                for r in range(3):
                    for c in range(3):
                        val = board[boxr*3+r][boxc*3+c]
                        if val != ".":
                            digits.append(val)
                if len(digits) != len(set(digits)):
                    return False
        
        return True
        


        # check every row, maybe try a set and remove all duplicates or do counter and count the number of periods
        # then see what the length of the set is. Set is unique numbers and one period. If length of set + # of periods -1 does not equal 9 then it has a repeat