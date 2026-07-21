class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # we can treat it all as one sequence and convert the indices to the 2d arrays indices
        # to get row its mid // n, n being the number of columns
        # to get columns its mid % n
        n = len(matrix[0])
        left = 0
        right = n * len(matrix) -1
        while left <=right:
            mid = left + (right-left)//2
            row = mid // n
            col = mid % n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = mid - 1
            elif matrix[row][col] < target:
                left = mid + 1
        return False
    