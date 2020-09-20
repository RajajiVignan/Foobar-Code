#I have tried Probability concepts to get the result instead of the markov chain concept. 
# Yes it is long process..:)
def gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a  
def lcm(a, b):
    return a * b / gcd(a, b)
def solution():
    p0 = 0
    p1 = 2
    p2 = 1
    p3 = 0
    p4 = 0
    p5 = 0
    q0 = 0
    q1 = 0
    q2 = 0
    q3 = 3
    q4 = 4
    q5 = 0
    s2_num =0
    s2_deno =0
    s3_num = 0
    s3_deno = 0
    s4_deno = 0
    s4_num =0
    i = 0
    sum1 = p0 + p1 +p2+p3+p4+p5
    sum2 = q0+q1+q2+q3+q4+q5
    Lcm = lcm(sum1,sum2)
    #first we need to check whether p1 = 0 but here i directly give the values.
    if p1 == 0:
        s2_num = p2
        s3_num = p3
        s4_num = p4
        s5_num = p5
        Grand_deno = sum1
    #for the following code p1 should always have some value
    # and i see that to avoid branching q0 should always be zero. 
    #calculating numerator and denominator for each S
    #starting with ---------------------------S2---------------------------------------
    if p0 == 0: 
        if p2 == 0 and q2 == 0: 
            s2_num = 0
            s2_deno = 1
        if p2 != 0 and q2 == 0:
            if q0 == 0 and q1 == 0: 
                temp_num = p2
                temp_deno = sum1
            if q0 != 0 and q1 == 0: 
                temp_num = p2 * Lcm
                temp_deno = sum1* (Lcm - (p1 * q0))
            if q0 == 0 and q1 != 0:
                temp_num = p2
                temp_deno = sum1 
        if p2 == 0 and q2 != 0: 
            if q0 == 0 and q1 == 0: 
                temp_num = p1*q2
                temp_deno = sum1*sum2
            if q0 != 0 and q1 == 0:
                temp_num = p1* q1* Lcm
                temp_deno = sum1*sum2*(Lcm-(p1*q0))
            if q0 == 0 and q1 != 0:
                temp_num = p1*q1*sum2
                temp_deno = sum1*sum2*(sum2-p2)
        #from the above code we get temp_num and temp_deno which can be converted into simplified fractions using gcd
        while i in range(100):
            x = gcd(temp_num,temp_deno)
            if x > 1: 
                temp_num = temp_num/x
                temp_deno = temp_deno/x
            if x ==1: 
                break
            x = gcd(temp_num,temp_deno)
        s2_num = temp_num
        s2_deno = temp_deno
    # now let us write code for------------------S3--------------------------------------------------
    if p0 == 0: 
        if p3 == 0 and q3 == 0: 
            s3_num = 0
            s3_deno = 1
        if p3 != 0 and q3 == 0:
            if q0 == 0 and q1 == 0: 
                temp_num = p3
                temp_deno = sum1
            if q0 != 0 and q1 == 0: 
                temp_num = p3 * Lcm
                temp_deno = sum1* (Lcm - (p1 * q0))
            if q0 == 0 and q1 != 0:
                temp_num = p3
                temp_deno = sum1 
        if p3 == 0 and q3 != 0: 
            if q0 == 0 and q1 == 0: 
                temp_num = p1*q3
                temp_deno = sum1*sum2
            if q0 != 0 and q1 == 0:
                temp_num = p1* q1* Lcm
                temp_deno = sum1*sum2*(Lcm-(p1*q0))
            if q0 == 0 and q1 != 0:
                temp_num = p1*q1*sum2
                temp_deno = sum1*sum2*(sum2-p3)
        #from the above code we get temp_num and temp_deno which can be converted into simplified fractions using gcd
        while i in range(100):
            x = gcd(temp_num,temp_deno)
            if x > 1: 
                temp_num = temp_num/x
                temp_deno = temp_deno/x
            if x ==1: 
                break
            x = gcd(temp_num,temp_deno)
        s3_num = temp_num
        s3_deno = temp_deno
    #now let's write code for--------------------S4----------------------------------------------------------------
    if p0 == 0: 
        if p4 == 0 and q4 == 0: 
            s3_num = 0
            s3_deno = 1
        if p4 != 0 and q4 == 0:
            if q0 == 0 and q1 == 0: 
                temp_num = p4
                temp_deno = sum1
            if q0 != 0 and q1 == 0: 
                temp_num = p4 * Lcm
                temp_deno = sum1* (Lcm - (p1 * q0))
            if q0 == 0 and q1 != 0:
                temp_num = p4
                temp_deno = sum1 
        if p4 == 0 and q4 != 0: 
            if q0 == 0 and q1 == 0: 
                temp_num = p1*q4
                temp_deno = sum1*sum2
            if q0 != 0 and q1 == 0:
                temp_num = p1* q1* Lcm
                temp_deno = sum1*sum2*(Lcm-(p1*q0))
            if q0 == 0 and q1 != 0:
                temp_num = p1*q1*sum2
                temp_deno = sum1*sum2*(sum2-p4)
        #from the above code we get temp_num and temp_deno which can be converted into simplified fractions using gcd
        while i in range(100):
            x = gcd(temp_num,temp_deno)
            if x > 1: 
                temp_num = temp_num/x
                temp_deno = temp_deno/x
            if x ==1: 
                break
            x = gcd(temp_num,temp_deno)
        s4_num = temp_num
        s4_deno = temp_deno

    #Grand denominator:
    temp_grand_deno = lcm(s2_deno,s3_deno)
    Grand_deno = lcm(temp_grand_deno,s4_deno)
    #print("s2 has numerator = {} and denominator= {}".format(s2_num,s2_deno))
    #print("s3 has numerator = {} and denominator= {}".format(s3_num,s3_deno))
    #print("s4 has numerator = {} and denominator= {}".format(s4_num,s4_deno))
    #print("Main denominator is {}".format(Grand_deno))
    
    #this code is incomplete. Need to add code for S5 to S9 and then take the output as a list. 
    #also need to write code for recursive lists since this code works for 2 sample cases only. 
