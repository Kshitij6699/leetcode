# link :- https://practice.geeksforgeeks.org/problems/the-painters-partition-problem1535/1
# n = 5
# k = 3
# arr[] = {5,10,30,20,15}
# Output: 35

# Search Space=> Range(max,sum) => we have to find minimum of all maximum possible solutions.

def isPossibleSolution(boards, k, mid):
    count = 1
    Tsum = 0
    n = len(boards)
    for i in range(n):
        if boards[i] > mid:
            return False
        if Tsum + boards[i] > mid:
            count += 1
            Tsum = boards[i]
            if count > k:
                return False
        else:
            Tsum += boards[i]
    return True
def findLargestMinDistance(boards:list, k:int):
    n = len(boards)
    start = max(boards)
    end = sum(boards)
    ans = start
    if n < k:
        return -1
    while(start <= end):
        mid  = (start + end)//2
        if isPossibleSolution(boards, k, mid):
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
    return ans