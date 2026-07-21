from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Solution 1 - Naive, one pass per requirement
        for row in board:
            seen = set()
            for col in row:
                if col != ".":
                    if col in seen:
                        return False
                    else:
                        seen.add(col)
        for col in range(len(board[0])):
            seen = set()
            for row in range(len(board)):
                val = board[row][col]
                if val != ".":
                    if val in seen:
                        return False
                    else:
                        seen.add(val)
                        
        seen = defaultdict(set)
        for row in range(len(board)):
            for col in range(len(board[0])):
                r = row // 3
                c = col // 3
                val = board[row][col]
                key = tuple([r, c])
                
                if val != ".":
                    if val in seen[key]:
                        return False
                    else:
                        seen[key].add(val)
        return True



        

                