class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for num in row:
                if num in seen and num != ".":
                    return False
                seen.add(num)
        for col in range(9):
            seen = set()
            for row in range(9):
                if board[row][col] in seen and board[row][col] != ".":
                    return False
                seen.add(board[row][col])
        # 9 boxes, 3 per row and 3 per col
        for i in range(3):
            for j in range(3):
                seen = set()
                for row in range(3):
                    for col in range(3):
                        num = board[row + 3*i][col + 3*j]
                        if num in seen and num != ".":
                            return False
                        seen.add(num)
        return True


