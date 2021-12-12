#!/usr/bin/env python3

def genTable(m, n):
    return [[0] * (n+1) for _ in range(m+1)]

def maxCut(m, n):
    print (m, n)
    if (m <= 0 or n <= 0):
        print("m or n < 0: m=" + str(m) + ", n=" + str(n)) 
        ##t[m][n] = 0
        return 0
    
    vMax = 0
    hMax = 0
    val = 0

    if t[m][n] != 0:
        print("table entry not -1, was: " + str(t[m][n]))
        return t[m][n]
    
    for c in C:
        print("in for: c=" + str(c))
        x = c[0]
        print("m - x = " + str(m - x))
        v = maxCut(m-x, n) + maxCut(x, n)
        if v > vMax:
            vMax = v
    
        y = c[1]
        print("n - y = " + str(n - y))
        h = maxCut(m, n-y) + maxCut(m, y)
        if h > hMax:
            hMax = h
        
        if c == (m, n):
            val = m * n
        
    
    mnMax = max(val, max(vMax, hMax))
    t[m][n] = mnMax
    return mnMax

m = 21
n = 11
C = {(10, 4), (6, 2), (7, 5), (15, 10)}

t = genTable(m, n)

mnMax = maxCut(m, n)

print(mnMax)
