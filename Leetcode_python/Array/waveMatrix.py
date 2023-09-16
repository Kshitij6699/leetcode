# Input: mat[][] =          [[1,2,3,4]
#                            [5,6,7,8]
#                            [9,10,11,12]
#                            [13,14,15,16]
#                            [17,18,19,20]]
# Output: 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19 20 16 12 8 4 
# Explanation: Output is printed in wave form. 


class Solution():
    def waveMatrix(self,lst):
        n = len(lst)
        m = len(lst[0])
        for col in range(m):
            if col % 2 == 0:
                for row in range(n):
                    print(lst[row][col],end=' ')
            else:
                for row in range(n-1,-1,-1):
                    print(lst[row][col],end=' ')

Input= [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]]
print(waveMatrix(Input))