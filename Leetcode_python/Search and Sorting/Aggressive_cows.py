# Link:- https://www.spoj.com/problems/AGGRCOW/
# stall = [1,2,8,4,9]
# cows = 3

# Given a list of elements indicating the number of stalls.
# we have to place the all the cows in those stall such that 
# the minimum distance between then is maximum possible distance.

# Method I - Brute fore :- Linear search O(n^2)
# we need the maximum distance of all those minimum distance permutations
# So we will traverse the array by checking 

# Method II- Binary Search nLog(n)
# 1.First, we will sort the given stalls[] array.
# 2.Place the 2 pointers i.e. low and high: Initially, we will place the pointers. The pointer low will point to 1 and the high will point to (stalls[n-1]-stalls[0]). As the ‘stalls[]’ is sorted, ‘stalls[n-1]’ refers to the maximum, and ‘stalls[0]’ is the minimum element.
# 3.Calculate the ‘mid’: Now, inside the loop, we will calculate the value of ‘mid’ using the following formula:
#   mid = (low+high) // 2 ( ‘//’ refers to integer division)
# 4.Eliminate the halves based on the boolean value returned by isPossibleSolution():
#     We will pass the potential distance, represented by the variable ‘mid’, to the ‘isPossibleSolution()‘ function. 
#     This function will return true if it is possible to place all the cows with a minimum distance of ‘mid’.
#     If the returned value is true: On satisfying this condition, we can conclude that the number ‘mid’ is one of our possible answers. 
#     But we want the maximum number. So, we will eliminate the left half and consider the right half(i.e. low = mid+1).
#     Otherwise, the value mid is greater than the distance we want. This means the numbers greater than ‘mid’ should not be considered and the right half of ‘mid’ consists of such numbers. So, we will eliminate the right half and consider the left half(i.e. high = mid-1).
# 5.Finally, outside the loop, we will return the value of high as the pointer will be pointing to the answer.


# --The steps from 3-4 will be inside a loop and the loop will continue until low crosses high.


class Solution:
    def isPossibleSolution(self,stall,c,k):
        count = 1
        last = stall[0]
        n = len(stall)
        for i in range(n):
            if stall[i] - last >= k:
                count += 1
                last = stall[i]
            if count >= c:
                return True
        return False
    # Linear Search
    # 
    # def aggressiveCows(self, stall, c):
    #     stall.sort()
    #     n =len(stall)
    #     limit = stall[n - 1] - stall[0]
    #     for i in range(1, limit + 1):
    #         if Solution().isPossibleSolution(self,stall,c,i) == False:
    #             return i - 1
    #     return limit

    # Binary Search 
    def aggressiveCows(self, stall, cows):
        stall.sort()
        n = len(stall)
        start = 1
        end = stall[n -1] - stall[0]
        while(start <= end):
            mid  = (end - start) // 2
            if Solution().isPossibleSolution(self,stall, cows,mid):
                start = mid + 1
            else:
                end = mid - 1
        return end
