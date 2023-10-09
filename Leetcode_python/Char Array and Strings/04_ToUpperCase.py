def toUpperCase(strings):
    str = ""
    i = 0
    while(i < len(strings)):
        if ord(strings[i]) >= 97  and ord(strings[i]) <= 122:
            word = strings[i]
            converted = chr(ord(word) -97 + 65)
            str += converted
        else:
            str += strings[i]
        i+=1
    return str