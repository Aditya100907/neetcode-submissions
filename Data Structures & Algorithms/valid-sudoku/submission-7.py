from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for col in row:
                if col in seen and col != ".":
                    return False
                else:
                    seen.add(col)
        for col in range(len(board[0])):
            seen = set()
            for row in range(len(board[0])):
                item = board[row][col]
                if item in seen and item != ".":
                    return False
                else:
                    seen.add(item)

        sub_box = defaultdict(set)
        for row in range(len(board)):
            for col in range(len(board[0])):
                r = row // 3
                c = col // 3
                val = board[row][col]
                key = tuple([r, c])
                if val != ".":
                    if val in sub_box[key]:
                        return False
                    else:
                        sub_box[key].add(val)
        return True



        

                