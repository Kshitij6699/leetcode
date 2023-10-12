# Link :- https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/description/
# Input: garbage = ["G","P","GP","GG"], travel = [2,4,3]
# Output: 21
# Explanation:
# The paper garbage truck:
# 1. Travels from house 0 to house 1
# 2. Collects the paper garbage at house 1
# 3. Travels from house 1 to house 2
# 4. Collects the paper garbage at house 2
# Altogether, it takes 8 minutes to pick up all the paper garbage.
# The glass garbage truck:
# 1. Collects the glass garbage at house 0
# 2. Travels from house 0 to house 1
# 3. Travels from house 1 to house 2
# 4. Collects the glass garbage at house 2
# 5. Travels from house 2 to house 3
# 6. Collects the glass garbage at house 3
# Altogether, it takes 13 minutes to pick up all the glass garbage.
# Since there is no metal garbage, we do not need to consider the metal garbage truck.
# Therefore, it takes a total of 8 + 13 = 21 minutes to collect all the garbage.

class Solution:
    def garbageCollection(self, garbage, travel):
        pickM, pickP, pickG= 0,0,0
        time_travelM, time_travelG, time_travelP = 0,0,0
        last_indexM, last_indexP, last_indexG = 0,0,0
        i = 0
        while( i < len(garbage)):
            ch = garbage[i]
            j = 0
            while j < len(ch):
                if ch[j] == 'P':
                    pickP += 1
                    last_indexP = i
                if ch[j] == 'G':
                    pickG += 1
                    last_indexG  = i
                if ch[j] == 'M':
                    pickM += 1
                    last_indexM = i
                j += 1
            i += 1

        i = 0
        while i < (last_indexP):
            time_travelP += travel[i]
            i += 1
        
        for i in range(last_indexG):
            time_travelG = time_travelG + travel[i]
        
        i = 0
        while i < (last_indexM):
            time_travelM += travel[i]
            i += 1
        
        ans = ( time_travelP + pickP) + ( time_travelG + pickG) + ( time_travelM + pickM )
        return ans