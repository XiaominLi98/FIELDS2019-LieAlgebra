# Check if a polynomial is symmetric
def checkSymmetric(poly):
    if poly != poly.subs(x=y, y=x):
        return False
    if poly != poly.subs(x=z, z=x):
        return False
    if poly != poly.subs(y=z, z=y):
        return False
    return True

import numpy as np

#Partition number n into k parts
def part(n, k):
    def _part(n, k, pre):
        if n <= 0:
            return []
        if k == 1:
            if n <= pre:
                return [[n]]
            return []
        ret = []
        for i in range(min(pre, n), 0, -1):
            ret += [[i] + sub for sub in _part(n-i, k-1, i)]
        return ret
    return _part(n, k, n)

#Partition number n into any number of parts
def partition(n):
    part3 = part(n,3)
    part2 = part(n,2)
    part1 = part(n,1)
    for ls in part2:
        ls.append(0)
    for ls in part1:
        ls += [0,0]


# Get all u such that sum(u) < sum(lambda)
def getMuLessThanLam(lams):
    count = 0
    ret = []
    s = sum(lams)
    print "All u such that sum(u)<sum(lambda):"
    for x1 in [0..s]:
        for y1 in [0..min(s-x1, x1)]:
            for z1 in [0..min(s-x1-y1, y1)]:
                if x1 > lams[0]:
                    continue
                if (x1,y1,z1)==lams:
                    continue
                else:
                    count += 1
                    ret.append((x1,y1,z1))
    
    # print "COUNT =", count
    return ret
   

# Return A > B in lex order
def lexBigger(A, B):
    (a1,a2,a3) = A
    (b1,b2,b3) = B
    
    if a1 > b1:
        return True
    elif a1==b1 and a2>b2:
        return True
    elif a1==b1 and a2==b2 and a3>b3:
        return True
    else:
        return False


# Return u < lowerU in lexicographical order, but 
# still the sum cannot be bigger than lams
def getLexLessThan(lowestU, lams): 
    count = 0
    ret = []
    print "All u s.t.lex(u)<lex(lowestU): (sum at least should < sum(lams))"
    
    
    for x1 in [0..lowestU[0]-1]:
        for y1 in [0..x1]:
            for z1 in [0..y1]:
                    if x1+y1+z1 > sum(lams):
                        continue
                    count += 1
                    ret.append((x1,y1,z1))
                    
                    
    for x1 in [lowestU[0]]:
        for y1 in [0..x1]:
            for z1 in [0..y1]:
                if lexBigger(lowestU, (x1,y1,z1)):
                    if x1+y1+z1 > sum(lams):
                        continue
                    count += 1
                    ret.append((x1,y1,z1))
    
    # print "COUNT =", count
    return ret
