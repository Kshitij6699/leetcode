# Link:- https://practice.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article
# Input:
# N = 4
# A[] = {12,34,67,90}
# M = 2
# Output:113

#Method I :- Brute force (Linear Search) O(N^2) for loop 
#Method II :- Binary search O(N*log(N))

# we have find the minimum of the all possible solutions.


# 1. If m > n: In this case, book allocation is not possible and so, we will return -1.
# 2. Place the 2 pointers i.e. low and high: Initially, we will place the pointers. The pointer low will point to max(arr[]) and the high will point to sum(arr[]).
# 3. Calculate the ‘mid’: Now, inside the loop, we will calculate the value of ‘mid’ using the following formula:
# mid = (low+high) // 2 ( ‘//’ refers to integer division)
# 4. Eliminate the halves based on the number of students returned by isPossibleSolution():
#     We will pass the potential number of pages, represented by the variable ‘mid’, to the ‘isPossibleSolution()‘ function. 
#     This function will return the number of students to whom we can allocate the books.
#     - If students > m: On satisfying this condition, we can conclude that the number ‘mid’ is smaller than our answer. So, we will eliminate the left half and consider the right half(i.e. low = mid+1).
#     - Otherwise, the value mid is one of the possible answers. But we want the minimum value. So, we will eliminate the right half and consider the left half(i.e. high = mid-1).
# 5. Finally, outside the loop, we will return the value of low as the pointer will be pointing to the answer.

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
        s = 0 # we also use s = max(A)
        end = sum(A)
        while (s <= end):
            mid  = int((s + end)/2)
            if(Solution().isPossibleSolution(A,N,M,mid)):
                ans = mid
                end = mid - 1
            else:
                s = mid + 1
        return ans

    #  Method I :- Linear Search
    # def isPossibleSolution(self, A, N , M ,solution):
    #     c = 1
    #     totalpages = 0
    #     for i in  range(len(A)):
    #         if(A[i] > solution):
    #             return -1
    #         if(A[i] + totalpages > solution ):
    #             c += 1
    #             totalpages = A[i]
    #         else:
    #             totalpages += A[i]
    #     return c

    # def findPages(self,A, N, M):
    #     if ( M > N):
    #         return -1
    #     start = max(A)
    #     end = sum(A)
    #     for i in range(start, end + 1):
    #         if Solution().isPossibleSolution == M:
    #             return i
    #     return start