class Solution:
    def transpose(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        ans = []
        for i in range(col):
            tmp = []
            for j in range(row):
                tmp.append(matrix[j][i])
            ans.append(tmp)
        return ans

input = [[1,2,3],[4,5,6],[7,8,9]]
print(Solution().transpose(input))