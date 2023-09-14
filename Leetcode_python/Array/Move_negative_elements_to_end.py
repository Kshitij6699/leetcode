# Input : 
# N = 8
# arr[] = {1, -1, 3, 2, -7, -5, 11, 6 }
# Output : 1  3  2  11  6  -1  -7  -5

class Solution:
    def segregateElements(self, arr, n):
        # Your code goes here
        lst = []
        for i in range(n):
            if arr[i] > 0:
                lst.append(arr[i])
        for i in range(n):
            if arr[i] < 0:
                lst.append(arr[i])
        for i in range(n):
            arr[i] = lst[i]
        return arr

input = [1, -1, 3, 2, -7, -5, 11, 6]
n = len(input)
print(Solution().segregateElements(input, n))