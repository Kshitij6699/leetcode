def findQuotient(dividend,divisor):
    s = 0
    e = dividend
    ans = -1
    if(divisor == 0):
        return "incorrect divisor"
    while(s<=e):
        mid = int(s + (e-s)/2)
        if(mid * divisor == dividend):
            return mid
        elif(mid * divisor > dividend):
            e = mid - 1
        else:
            ans = mid
            s = mid + 1
    return ans

dividend = 29
divisor = -7
ans = findQuotient(abs(dividend),abs(divisor))
if (dividend < 0 or divisor < 0 ):
    ans = -1 * ans
print(ans)