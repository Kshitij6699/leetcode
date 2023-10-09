def reverse(s):
    i = 0
    j = len(s) - 1
    str = ''
    while(j >=0):
        str += s[j]
        j-=1
    return str

#string doesn't support item assignment means it is immutable.