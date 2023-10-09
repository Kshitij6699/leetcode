def toLowerCase(string):
    str = ""
    i = 0
    while(i < len(string)):
        #check if upper case, to convert tit to lowercase
        if(ord(string[i]) >= 65 and ord(string[i]) <= 90):
            word  = string[i]
            converted  = chr(ord(word) - 65 + 97)
            str += converted
        else: str += string[i]
        i += 1
    return str
