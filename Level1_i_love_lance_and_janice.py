def solution(s):
    #creating a function to extract character out of string
    def split(word):
        return [char for char in word]
    r = split(s)
    d = ''
    for i in s:
        x = i
        if ord(x) >= 97 and ord(x) <= 122:
                y = 122 - ord(x)
                #using ord we get the ascii number of the character stored in the variable(x)
                char = chr(97+y)
                #char is used to get character from the ascii number.
                d += char    
        else:
            d+= i    
    return(d)