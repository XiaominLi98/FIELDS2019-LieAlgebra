#Deep copy a list of list
def getCopy(lsOfls):
    ret = []
    for ls in lsOfls:
        ret.append(copy(ls)) 
    return ret

#If needed, remove 'None" in a list of list (see "getTab12(tList)")
def removeNone(tList):
    tListCopy = getCopy(tList)
    tList = []
    for idx, row in enumerate(tListCopy):
        newRow = []
        for e in row:
            if e!=None:
                newRow.append(e)
        tList.append(newRow) #we need to keep [] for the u tableau later
    return tList

        
#x1 is x; x2 is y; x3 is z
def xi(i):
    if i == 1:
        return x-2*k
    elif i == 2:
        return y-k
    return z

#a'(s)
def aprime(s): # position s = tuple (i,j)
    (i,j) = s #Xiaomin: Notice i,j should start with 1, so we add 1 below:
    return (j+1)-1
#l'(s)
def lprime(s): # position s = tuple (i,j)
    (i,j) = s #Xiaomin: Notice i,j should start with 1, so we add 1 below:
    return (i+1)-1



#-------Calculate lambda^(0)=T, lambda^(1), lambda^(2), lambda^(3)={} ---------

#Return the locations (i,j) of boxes s in a tableau
def getTabPos(tabi):
    ret = []
    for r in range(len(tabi)):
        for c in range(len(tabi[r])):
            if tabi[r][c] != None:
                ret.append((r,c))
    return ret


#Return  tableaus lambda^(0)=T, lambda^(1), lambda^(2), lambda^(3)={}
# and the locations of their boxes
def getTab12(tList):
    T = Tableau(tList)
    tab12 = []
    tab12Pos = []
    for i in [1,2]:
        tabi = T.anti_restrict(i)
        tabi = tabi.to_list()
        tabiPos = getTabPos(tabi)
        
#         tabi = removeNone(tabi) 
#Xiaomin: if needed, could keep the 'None'. 
# This is more for display purpose

        tab12.append(tabi)
        tab12Pos.append(tabiPos)
    return (tab12, tab12Pos)



#-----------------------Calculate  R/C... ----------------------
#We use two boolean markers to mark if a box satisfies properties or not.

#Initialize the markers for proerty 1 and proerty 2 (all boxes have ``False")
def initializeProperty12Marker(tabi):
    marker = []
    for i,row in enumerate(tabi):
        newRow = []
        for e in row:
            if e!=None:
                newRow.append(False)
        if newRow != []:    
            marker.append(newRow)
    marker2 = getCopy(marker)
    return marker, marker2 

#count number of boxes in row with index = rowIdx
def countRowIdx(tabiPos, rowIdx):
    count = 0
    for (i,j) in tabiPos:
        if i==rowIdx:
            count += 1
    return count
    
#count number of boxes in row with index = colIdx
def countColumnIdx(tabiPos, colIdx):
    count = 0
    for (i,j) in tabiPos:
        if j==colIdx:
            count += 1
    return count
    
#Mark boxes by property1    
def updateProperty1Marker(tList, tabiPos, tabiMinus1Pos, property1Marker):
    for rowIdx in range(len(property1Marker)):
        countI = countRowIdx(tabiPos, rowIdx)
        #count (rowIdx, ?) from tabiPos = num of boxes in tabi for row idx 
        countIMinus1 = countRowIdx(tabiMinus1Pos, rowIdx)
        #similar, count row idx elements in tabiMinus1
        
        if countIMinus1 > countI: #then all s in this row has property1
            property1Marker[rowIdx] = [True for ij in property1Marker[rowIdx]]
            #update this row!

    
#Mark boxes by property2   
def updateProperty2Marker(tList, tabiPos, tabiMinus1Pos, property2Marker):
    if property2Marker==[]:
        return
    for colIdx in range(len(property2Marker[0])):
        countI = countColumnIdx(tabiPos, colIdx)
        #count (colIdx, ?) from tabiPos = num of boxes in tabi for column idx 
        countIMinus1 = countColumnIdx(tabiMinus1Pos, colIdx)
        #similar, count column idx elements in tabiMinus1
        
        if countIMinus1 <= countI: #then all s in this column has property 2
            for i in range(len(property2Marker)):
                if len(property2Marker[i]) >= (colIdx+1):
                    property2Marker[i][colIdx] = True #update this row!

    
#Return R/C_(i-1)/i i=1,2,3
def getRCi(tList, allTab, allTabPos, i):
    tabiPos = allTabPos[i]
    tabiMinus1Pos = allTabPos[i-1]
    RCi = []
    
    property1Marker, property2Marker = initializeProperty12Marker(allTab[i])
    updateProperty1Marker(tList, tabiPos, tabiMinus1Pos, property1Marker)
    updateProperty2Marker(tList, tabiPos, tabiMinus1Pos, property2Marker)
    
    for (i,j) in tabiPos: #since all s in R/C come from tableau i
        if property1Marker[i][j]==False:
            continue
        if property2Marker[i][j]==False:
            continue
        RCi.append((i,j))
    return RCi

        


#-----------------------Calculate  psi_T(k) ----------------------

# psi_T(k)
def psi(tList):
    
    # Get Tableau lambda^(0),lambda^(1),lambda^(2),lambda^(3)
    tab0 = tList #Young diagram with boxes of numbers 1,2,3
    (tab1, tab2), (tab1Pos, tab2Pos) = getTab12(tList)
    #tab1 = Young diagram with boxes of numbers 2,3
    #tab2 = Young diagram with boxes of numbers 3
    tab3 = {}
    allTab = [tab0, tab1, tab2, tab3]
    
    # Get Tableau positions (i,j)
    tab0Pos = getTabPos(allTab[0])
    tab3Pos = getTabPos(allTab[3])
    allTabPos = [tab0Pos, tab1Pos, tab2Pos, tab3Pos]

    
    # Now calculate all RC
    allRC = []
    for i in [1,2,3]:
        RCi = getRCi(tList, allTab, allTabPos, i)
        allRC.append(RCi)

        
    # Finally, calculate psi_T(k)
    ret = 1
    for i in [1,2,3]:
        for s in allRC[i-1]: #since the first of allRC is allRC[0]
            tabi = allTab[i]
            tabiMinus1 = allTab[i-1]
            tabi = removeNone(tabi)
            tabiMinus1 = removeNone(tabiMinus1)
            
            ret *=  b(tabi, s, k) / b(tabiMinus1, s, k)  #s = position (i,j)
    return ret

#b_u(s,k)
def b(u, s, k): #u is a Young diagram. 
    aa = a(u, s)
    ll = l(u, s)
    return (aa + k*(ll+1)) / (aa + k*ll + 1)
#a_(s)
def a(u, s):
    (i,j) = s
    return len(u[i]) - (j+1) #Xiaomin: Notice i,j should start with 1
#l_(s)
def l(u, s):
    (i,j) = s
    i+=1; j+=1 #Xiaomin: Notice i,j should start with 1
    
    count = 0
    for m in range(i+1, 4):  #i < m <=3
        if len(u)>=m and len(u[m-1]) >= j:
            count += 1
    return count


#-------Find all valid filling (reverse tableau) of 3,2,1----------------


#Initialize unfilledPositionsStart, return the list of all positions
def initUnfilledPositionsStart(tListStart):
    unfilledPositionsStart = []
    for i in range(len(tListStart)):
        for j in range(len(tListStart[i])):
            unfilledPositionsStart.append((i,j))
    return unfilledPositionsStart



#Fill entry (i,j) with num
def fillEntry(i,j,num, tList, unfilledPositions, allFilledLists):
    #fill num into entry i,j:
    copyList = getCopy(tList)
    copyList[i][j] = num

    #pop unfilledPositions:
    copyUnfilledPositions = copy(unfilledPositions)
    copyUnfilledPositions.pop(0)
        
    #continue fill:
    fill(copyList, copyUnfilledPositions, allFilledLists)

   
# Fill the whole tableau with numbers 1,2,3
def fill(tList, unfilledPositions, allFilledLists):    
    #-------------Done! return--------------
    if len(unfilledPositions) == 0: 
        allFilledLists.append(tList)
        return
    
    
    #---------------Fill:------------------
    (i,j) = unfilledPositions[0]
    if i==0: #1st row
        if j==0:
            for num in [3,2,1]:
                fillEntry(i,j,num, tList, unfilledPositions, allFilledLists)  
        else: #j>0:
            reverseRange = range(1, tList[i][j-1]+1)
            reverseRange.reverse()
            for num in reverseRange:
                fillEntry(i,j,num, tList, unfilledPositions, allFilledLists)  
    
    else: #2nd or 3rd row
        if j==0:
            for num in [3,2,1]:
                if num < tList[i-1][j]: # compare with the "up" neighber
                    fillEntry(i,j,num, tList, unfilledPositions, allFilledLists)  
        else: #j>0:
            reverseRange = range(1, tList[i][j-1]+1)
            reverseRange.reverse()
            for num in reverseRange:
                if num < tList[i-1][j]:
                    fillEntry(i,j,num, tList, unfilledPositions, allFilledLists)  
      
                

# Plot the filled tableaus
def plotTabs(allFilledLists):
    tableaus = []
    for tList in allFilledLists:
        T = Tableau(tList)
        tableaus.append(T)
        show(T.plot(descents=False))
    #     print ascii_art(T), "\n"
    print "count tableaus = ", len(tableaus)


# Get all Reverse Tableaus of filling 1,2,3 
def getAllReverseT(allLambda):
    tListStart = []
    for i in range(3):
        if allLambda[i]!=0:
            tListStart.append([None for i in range(allLambda[i])])

    unfilledPositionsStart = initUnfilledPositionsStart(tListStart) 
    
    allFilledLists = []   # will store all Reverse Tableaus of filling 1,2,3
    fill(tListStart, unfilledPositionsStart, allFilledLists)
    
    return allFilledLists




#Given lambda = (lambda1, lambda2, lambda3). 
# Already know lambda1 >= lambda2 >= lambda3 >=0

# -------MAIN: All fillings will be stored into "allFilledLists"-----

def getPHelper(allFilledLists, plot):
    P = R(0) # poly ring
    if plot:
        print "count tableaus = ", len(allFilledLists)
    for T in allFilledLists:
        currT = 1
        for i in range(len(T)):
            for j in range(len(T[i])):
                s = (i,j)
                currT *= (xi(T[i][j]) - aprime(s) + lprime(s)*k)
        P += currT * psi(T)
        if plot:
            print "======================================\n***Curr Tableau is:"
            show(Tableau(T).plot(descents=False))
            print "its polynomial is = "
            show(currT)
            print "======================================"
    return P



def getAnswer(allLambda, plot):
    allFilledLists = getAllReverseT(allLambda)
#     print "After filling, allFilledLists =", allFilledLists

    answer = getPHelper(allFilledLists, plot)
    return answer









#Main code to set up environment=============================================

# # T.<k> = QQbar[] 
#Xiaomin: 1. construct a rational field of variable 'k'
# T.<k> = ZZ[] 
#Xiaomin: 1. construct a rational field of variable 'k'

# FT = FractionField(T) 
#Xiaomin: 2. Extend it to a rational function field of 'k'
# # FT = T

# R.<x,y,z> = PolynomialRing(FT, order='lex') 
#Xiaomin: polynomial of x,y,z over 'FT' (rational function field of 'k')
# # print R
# F = FractionField(R) #  
#Xiaomin: extend the x,y,z polynomial ring to a rational function field


# # print F

# #-------------above is just to construct correct ring or field---------------
# pDict = {}
# tripleDict = {}


# # pDictSmall = {}

# # import time
# # start_time = time.time()
# # %store -r pDictSmall
# # print "pDictSmall retrieve done"
# # print("---took time  %s seconds ---" % (time.time() - start_time))



# # start_time = time.time()
# # %store -r tripleDict
# # print "tripleDict retrieve done"
# # print("---took time %s seconds ---" % (time.time() - start_time))







