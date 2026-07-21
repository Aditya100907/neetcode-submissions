from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Solution 2 - One pass total
        sub_seen = defaultdict(set)
        for row in range(len(board)):
            rseen = set()
            cseen = set()
            for col in range(len(board[0])):
                rval = board[row][col]
                cval = board[col][row]
                if rval != ".":
                    if rval in rseen:
                        return False
                    else:
                        rseen.add(rval)
                if cval != ".":
                    if cval in cseen:
                        return False
                    else:
                        cseen.add(cval)
                r = row // 3
                c = col // 3
                val = board[row][col]
                key = tuple([r, c])
                if val != ".":
                    if val in sub_seen[key]:
                        return False
                    else:
                        sub_seen[key].add(val)

        return True
    
        # # Solution 1 - Naive, one pass per requirement
        # for row in board:
        #     seen = set()
        #     for col in row:
        #         if col != ".":
        #             if col in seen:
        #                 return False
        #             else:
        #                 seen.add(col)
        # for col in range(len(board[0])):
        #     seen = set()
        #     for row in range(len(board)):
        #         val = board[row][col]
        #         if val != ".":
        #             if val in seen:
        #                 return False
        #             else:
        #                 seen.add(val)

        # seen = defaultdict(set)
        # for row in range(len(board)):
        #     for col in range(len(board[0])):
        #         r = row // 3
        #         c = col // 3
        #         val = board[row][col]
        #         key = tuple([r, c])
                
        #         if val != ".":
        #             if val in seen[key]:
        #                 return False
        #             else:
        #                 seen[key].add(val)
        # return True



        

                