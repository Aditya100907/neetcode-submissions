class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find some way to represent 2d matrix and one long sequence
        # compute the middle value for binary search in that one long sequence and convert it to a row col combo
        # keep going until is found or gone through entire array and not found, two pointers are equal to each other
        left = 0
        right = len(matrix) * len(matrix[0]) - 1

        while left <= right:
            mid = left + (right-left) // 2
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])
            if matrix[row][col]== target:
                return True
            elif matrix[row][col]< target:
                left = mid + 1
            else:
                right = mid -1
        return False