# Return the leading monomial and the degrees of x,y,z in it.
def getLmAndDegs(poly):
    lm = poly.lm()
    lc = poly.lc()

    xdeg = lm.degree(x)
    ydeg = lm.degree(y)
    zdeg = lm.degree(z)

    return lm, lc, (xdeg,ydeg,zdeg)


    return part1 + part2 + part3

#Return the linear combination for dP_lambda
def getLinearComb(P):
    diffP = diff(P, k)
    poly = diffP

    # triples of (coef, u, Pu)--changed to tuple of (coef, u)
    ret = []

    while poly != 0:
        
        lm, lc,degs = getLmAndDegs(poly)
        Pu = getAnswer(degs, plot=False)
        Pu *= x^0 #Xiaomin: for the integers to have type "polynomial"
        coef1 = lc
        coef2 = Pu.monomial_coefficient(lm)
        coef = coef1 / coef2

        ret.append((coef,degs))
        poly = poly - coef * Pu
    
    return ret

