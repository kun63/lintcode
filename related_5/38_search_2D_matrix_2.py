class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        result = 0
        n = len(matrix)
        m = len(matrix[0])
        limit_j = m
        for i in range(n):
            for j in range(m):
                if j >= limit_j:
                    break
                if matrix[i][j] == target:
                    result += 1
                    limit_j = j
                    break
                elif matrix[i][j] > target:
                    limit_j = j
                    break
        return result
    def _searchMatrix(self, matrix, target):
        if matrix == [] or matrix[0] == []:
            return 0
            
        row, column = len(matrix), len(matrix[0])
        i, j = row - 1, 0
        count = 0
        while i >= 0 and j < column:
            if matrix[i][j] == target:
                count += 1
                i -= 1
                j += 1
            elif matrix[i][j] < target:
                j += 1
            elif matrix[i][j] > target:
                i -= 1
        return count