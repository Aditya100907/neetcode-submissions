class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # len(matrix[0])* len(matrix) = how long the array is if it were 1D
        # 4 // len(matrix[0]) = row
        # 4 % len(matrix[0]) = col
        left = 0
        right = len(matrix[0])* len(matrix)-1
        while left <=right:
            mid = left + (right - left) // 2 # understand why
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = mid-1
            else:
                left = mid+1
        return False
