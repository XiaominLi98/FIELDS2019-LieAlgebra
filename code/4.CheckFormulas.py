import math
def fac(x):
    return math.factorial(x)*k^0




# (D,0,0) -> (u1,0,0) #old name: formula1_1
def formula1(lam, u):
    D,D2,D3 = lam
    u1,u2,u3 = u

    numerator = (-1)^(D-u1) * fac(D) / (fac(u1)*(D-u1))
    
    # (2*k+u1)..(2*k+D-1)
    part2k = 1
    for n in [(2*k+u1)..(2*k+D-1)]:
        part2k *= n
    
    #  (*k+u1)..(k+D-1)
    partk = 1
    for n in [(k+u1)..(k+D-1)]:
        partk *= n
        
    return numerator * (part2k+partk) / partk
    
    
# (D,0,0) -> (u1,u2,0) #old name: formula1_2
def formula2(lam, u):
    D,D2,D3 = lam
    u1,u2,u3 = u
    
#     -----------numerator------------
    numerator = (-1)^(D-u1+u2) * fac(D)*fac(D-u1-1) / (fac(D-u1-u2)*fac(u1-u2)*fac(u2))
    
#     -----------denominator----------
    denominator = 1
    #(k+u1-u2+1)..(k+u1)
    for n in [(k+u1-u2+1)..(k+u1)]:
        denominator *= n
    
    #(k+D-u2)..(k+D-1)
    for n in [(k+D-u2)..(k+D-1)]:
        denominator *= n

    return numerator/denominator



# (D,0,0) -> (u1,u2,u3) #old name: formula1_3
from scipy.special import comb
def formula3(lam, u): 
    D,D2,D3 = lam
    u1,u2,u3 = u

#     -----------numerator------------
#   Constant Part
    const = (-1)^(D-u1+u2) * fac(D)*fac(u2-1) / (fac(u1-u2)*fac(u2-u3)*fac(u3))


#   (k-u3+1)..k
    partkUp = 1
    for i in [(k-u3+1)..k]:
        partkUp *= i
        
#   (k-u3+1)..k
    partkUp2 = 1
    for i in [(k+u1-u3+1)..(k+u1-1)]:
        partkUp2 *= i


#   lastPart
    lastPart = 0
    for j in [0..D-u1-u2-u3]:
        curr = Integer(comb(D-u1-u2-1-j,u3-1))  *  Integer(comb(j+u2-1,j))
        for n in [(2*k+u1)..(2*k+ D-u2-u3-1 -j)]:
            curr *= n
        for n in [(k+ D-u2-j)..(k+ D-u2-1)]:
            curr *= n
        lastPart += curr    
        

#     -----------denominator----------

#   (k+u1-u2+1)..(k+D-1)
    partDown1 = 1
    for i in [(k+u1-u2+1)..(k+D-1)]:
        partDown1 *= i

#   (k+u2-u3+1)..(k+u2)
    partDown2 = 1
    for i in [(k+u2-u3+1)..(k+u2)]:
        partDown2 *= i

#   (2k+u1-u3+1)..(2k+u1)
    part2k = 1
    for i in [(2*k+u1-u3+1)..(2*k+u1)]:
        part2k *= i

    return (const*partkUp*partkUp2*lastPart) / (partDown1*partDown2*part2k)




# (D1,1,0) -> (u1,0,0) #old name: formula2_1
def formula4(lam, u):
    D1,D2 = lam[0],lam[1]
    u1,u2,u3 = u
    
    
#Case 1: D1-u1==0
    if D1-u1==0:
        return (-1)^D2 * fac(D2-1)

    
#Case 2: D1-u1>0
    numerator = (-1)^(D1-u1) * fac(D1-D2) / fac(u1) *  k*(k-1)
    # (2*k+u1)..(2*k+D1-2)
    for n in [(2*k+u1)..(2*k+D1-D2-1)]:
        numerator *= n

    denominator = 1
    for n in [(k+u1-1)..(k+D1-2)]:
        denominator *= n
    
    return numerator / denominator





# (D1,2,0) -> (u1,0,0) #old name: formula2_2
def formula5(lam, u):
    D1,D2 = lam[0],lam[1]
    u1,u2,u3 = u
    
    
#Case 1: D-u1==0
    if D1-u1==0:
        return (-1)^D2 * fac(D2-1)

    
#Case 2: D1-u1>0
    numerator = (-1)^(D1-u1) * fac(D1-D2) / fac(u1) *  k*(k-1)
    # (2*k+u1)..(2*k+D1-3)
    for n in [(2*k+u1)..(2*k+D1-D2-1)]:
        numerator *= n
    lastPart = (D1-u1-1)*k^2 - (3*D1+u1-3)*k - 2*(D1-1)*(u1-1)
    numerator *= lastPart
        
        
    denominator = 1
    # (k+u1-2)..(k+D1-3)
    for n in [(k+u1-D2)..(k+D1-D2-1)]:
        denominator *= n
    
    # (2k+D1-2)..(2k+u1-1)
    for n in [(2*k+D1-D2)..(2*k+u1-1)]:
        denominator *= n
    
    return numerator / denominator



# (D1,3,0) -> (u1,0,0) #old name: formula2_3
def formula6(lam, u):
    D1,D2 = lam[0],lam[1]
    u1,u2,u3 = u
    
    
#Case 1: D1-u1==0
    if D1-u1==0:
        return (-1)^D2 * fac(D2-1)

    
#Case 2: D1-u1>0
    numerator = (-1)^(D1-u1) * fac(D1-D2) / fac(u1) *  k*(k-1)  * fac(D2-1)
    # (2*k+u1)..(2*k+D1-4)
    for n in [(2*k+u1)..(2*k+D1-D2-1)]:
        numerator *= n

    lastPart = (D1-u1-2)*(D1-u1-1)/2 * k^4
    lastPart += -4*(D1-u1-1)*(2*D1+u1-4)/2 * k^3
    lastPart += +((6*D1-7)*u1^2+ (-6*D1^2+ 14*D1-9)*u1+ 23*(D1-2)*(D1-1))/2 * k^2
    lastPart += +((6*D1-10)*u1^2+ (18*D1^2-64*D1+ 54)*u1-28*(D1-2)*(D1-1))/2 * k
    lastPart += +6*(u1-2)*(u1-1)*(D1-2)*(D1-1)/2
    numerator *= lastPart
        
        
    denominator = 1
    # (k+u1-3)..(k+D1-4)
    for n in [(k+u1-D2)..(k+D1-D2-1)]:
        denominator *= n
    # (2k+D1-3)..(2k+u1-1)
    for n in [(2*k+D1-D2)..(2*k+u1-1)]:
        denominator *= n
    
    return numerator / denominator


# Since formula3: (D1,D2,0) -> (u1,u2,0) has many conditions, we leave it out here
# we will write it here after we have a full formula for it


#================================================================================
def CheckFormulas(lam, u):
    D1,D2,D3 = lam
    u1,u2,u3 = u
    
    if D3>0:
        return None
    
    # (D1,D2,0) -> u
    if D2 > 0:
        if u2>0:
            return None #(we only have formulas for ())
        if D2==1:
            return formula4(lam,u) #(D1,1,0) -> (u1,0,0)
        elif D2==2:
            return formula5(lam,u) #(D1,2,0) -> (u1,0,0)
        elif D2==3:
            return formula6(lam,u) #(D1,3,0) -> (u1,0,0)
    
    # (D1,0,0) -> u
    else: #D2==0:
        if u3>0:
            return formula1(lam,u) #(D1,D2,0) -> (u1,u2,u3)
        elif u2>0:
            return formula2(lam,u) #(D1,D2,0) -> (u1,u2,0)
        else:
            return formula3(lam,u) #(D1,D2,0) -> (u1,0,0)
    return None





#Main code to check formulas
# D2 = 0
# for D in [D2..13]:
#     lam = (D,D2,0)
#     print "-----------------lam=",lam,"---------------"
#     # P = getAnswer(lam, False)
#     # for (coef, u) in getLinearComb(P):
#     for (coef, u) in tripleDict[lam]:
#         D,D2,D3 = lam
#         u1,u2,u3=u
#         conjCoef = CheckFormulas(lam, u)
#         print coef==conjCoef
#         if coef!=conjCoef:
#             print("***coef   =", coef, ",   u = ", u)
#             print("conjCoef  =", conjCoef, ",   u = ", u)