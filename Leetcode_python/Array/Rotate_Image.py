#link:- https://leetcode.com/problems/rotate-image/description/
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
class Solution:
    def rotateMatrix(self,matrix: List[List[Int]]) -> None:
        n = len(matrix[0])
        #Step 1 : -take transpose
        for i in range(n):
            for j in range(i,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        #step 2 : -reverse array
        l = 0
        r = n - 1
        while(l<r):
            matrix[l],matrix[r] = matrix[l],matrix[r]

        return matrix
input = [[1,2,3],[4,5,6],[7,8,9]]
print(Solution().rotateMatrix(input))
print(input)