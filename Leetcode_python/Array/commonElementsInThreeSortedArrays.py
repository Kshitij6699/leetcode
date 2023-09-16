# Link : - https://practice.geeksforgeeks.org/problems/common-elements1132/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article
# n1 = 6; A = {1, 5, 10, 20, 40, 80}
# n2 = 5; B = {6, 7, 20, 80, 100}
# n3 = 8; C = {3, 4, 15, 20, 30, 70, 80, 120}
# Output: 20 80
# Explanation: 20 and 80 are the only common elements in A, B and C.

class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        ls = []
        i =0
        j = 0
        k = 0
        while(i<n1 and j < n2 and k < n3):
            if (A[i] == B[j] and B[j] == C[k]):
                if(len(ls) == 0 or ls[len(ls)-1] != A[i]):
                    ls.append(A[i])
                i+=1
                j+=1
                k+=1
            elif (A[i] < B[j]):
                i+=1
            elif (B[j] < C[k]):
                j+=1
            else:
                k+=1
        return ls
n1 = 6 
A = [1, 5, 10, 20, 40, 80]
n2 = 5
B = [6, 7, 20, 80, 100]
n3 = 8
C = [3, 4, 15, 20, 30, 70, 80, 120]
print(Solution().commonElements(A, B, C, n1, n2, n3))