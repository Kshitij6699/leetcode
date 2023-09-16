# link: -https://leetcode.com/problems/spiral-matrix/description/
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

class Solution:
    def spiralOrder(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        top, bottom, left, right = 0, n-1, 0, m-1
        result = []
        while len(result) < n*m:
            for i in range(left,right+1):
                result.append(matrix[top][i])
            top += 1
            for i in range(top, bottom+1):
                result.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for i in range(right,left-1,-1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            
            if left <= right:
                for i range(bottom,top-1,-1):
                    result.append(matrix[i][left])
                left += 1
        return result
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(Solution().spiralOrder(matrix))