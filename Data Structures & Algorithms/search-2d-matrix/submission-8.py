class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # naive - convert 2d matrix into 1d (takes O(n) space) and then do binary search for log mxn time complexity
        # could figure out a way to just search within the 2d matrix for O1 space complexity
        # need some rep of rows and cols: num // len(matrix[0]) for row, num % len(matrix[0]) for col
        left, right = 0, len(matrix[0])*len(matrix)-1
        while left <= right:
            mid = left + (right - left) // 2
            num = matrix[mid // len(matrix[0])][mid % len(matrix[0])]
            if num == target:
                return True
            elif num > target:
                right = mid-1
            else:
                left = mid + 1
        return False