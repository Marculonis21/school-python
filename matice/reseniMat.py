#!/usr/bin/env python3

from novaMat import *

gZero = 1/100

def gem(a):
    col = len(a[0])
    row = len(a)

    actRow = 0
    
    newMat = [[0.0 for x in range(col)] for y in range(row)]
    num = 0
    for loop in range(row-1):
        for y in range(loop,row):
            for x in range(col):
                if(actRow == y):
                    newMat[y][x] = a[y][x]
                else:
                    if(x == actRow):
                        num = a[y][x] / (a[actRow][x])

                    a[y][x] += a[actRow][x]*(-num)
                    newMat[y][x] = a[y][x]

        print(newMat)
        actRow += 1

    return newMat

def jem(a):
    col = len(a[0])
    row = len(a)

    newMat = [[0.0 for x in range(col)] for y in range(row)]
    num = 0
    
    actRow = row-1
    for loop in range(row-1):
        for y in reversed(range(row)):
        
            for x in range(col):
                if(actRow == y):
                    newMat[y][x] = a[y][x]
                else:
                    if(x == actRow):
                        num = a[y][x] / (a[actRow][x])
                    
                    a[y][x] += a[actRow][x]*(-num)
                    newMat[y][x] = a[y][x]

            printMat(newMat,True)
            print()
            print("num"+str(num))
            print()

        print(y,actRow)
        actRow -= 1

    for y in range(row):
        for x in range(col):
            if(newMat[y][x] != 0.0):
                num = newMat[y][x]
                newMat[y][x]/=num
                newMat[y][col-1]/=num
                
    return newMat    
    

if __name__ == "__main__":
    print("Hello World")

    matX = rozsirena()

    A = gem(matX)
    printMat(A,True)

    print()
    print("---")
    b = jem(A)
    printMat(b,True)    

    
