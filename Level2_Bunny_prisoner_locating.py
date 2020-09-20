def solution(x,y):
    n= x
    m = y + (x-2)
    l = n*(n+1)/2
    #we are locating the column of our minion
    z=  l+ m*(m+1)/2 - n*(n-1)/2
    #we are locating the id of our minion
    z= int(z)
    return z 
