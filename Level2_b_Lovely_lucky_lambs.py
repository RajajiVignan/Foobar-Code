def solution(total_lambs):
    a = [1,1]
    c = []
    Max =0
    Min =2
    z = 0
    if total_lambs < 10:
        print(0)
    if total_lambs > 10**9:
        print(0)
    i = 2
    while i <= total_lambs:
        b = a[i-1] + a[i-2]
        y = i
        Min += b
        a.append(b)  
        if Min > total_lambs:
            break
        i = i+1
    j = 0
    while j <= total_lambs:
        z= 2**j
        c.append(z)
        Max+= z
        if Max> total_lambs:
            break
        j = j+1
    solution = (len(a)-1) - (len(c)-1)
    return(abs(solution))
