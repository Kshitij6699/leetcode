# Link:- https://practice.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article
# Input:
# N = 4
# A[] = {12,34,67,90}
# M = 2
# Output:113


class Solution: 
    #Function to find minimum number of pages.
    def isPossibleSolution(self, A, N , M ,solution):
        c = 1
        totalpages = 0
        for i in  range(len(A)):
            if(A[i] > solution):
                return False
            if(A[i] + totalpages > solution ):
                c += 1
                totalpages = A[i]
                if(c > M):
                    return False
            else:
                totalpages += A[i]
        return True
    def findPages(self,A, N, M):
        #code here
        if(M > N):
            return -1
        ans = -1
        s = 0
        end = sum(A)
        while (s <= end):
            mid  = int((s + end)/2)
            if(Solution().isPossibleSolution(A,N,M,mid)):
                ans = mid
                end = mid - 1
            else:
                s = mid + 1
        return ans
