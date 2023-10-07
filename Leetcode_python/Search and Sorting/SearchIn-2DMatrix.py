# link:-https://leetcode.com/problems/search-a-2d-matrix/description/
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

# Behind scenes a 2-D matrix is stored in 1-D Array.
# So to calculate the indexes for a element in 2-D array, we need to do following:-
# for row, i = index / (column.size) .
# for columns, j = index % (column.size) .

class Solution:
    def searchMatrix(self, matrix, target):
        row = len(matrix)
        col = len(matrix[0])
        s = 0
        e = row*col - 1
        mid = int(s + (e-s)/2)

        while(s<=e):
            mid = int(s + (e-s)/2)
            i = int(mid/col)
            j = int(mid%col)

            if(matrix[i][j] == target):
                return True
            elif(matrix[i][j] > target):
                e = mid - 1
            else:
                s = mid + 1
        
        return False