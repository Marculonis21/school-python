#!/usr/bin/env python3

from novaMat import *

def matCompatibility(a,b):
    if(len(a[0]) == len(b)):
        return True
    else:
        return False

def nasobeni(a,b):
    mat = []

    for i in range(len(a)):
        radek=[]
        for j in range(len(b[0])):
            s=0
            for p in range(len(a)):
                s+=A[i][p]*B[p][j]
            radek += [s]
        mat += [radek]
    return mat  
    #dopsat ještě ne
    
    

if __name__ == "__main__":
            
    A = makeMat()
    print(A)
    print(len(A[0]))

    B = makeMat()
    print(B)
    print(len(B))

    fififi = matCompatibility(A,B)
    if(fififi):
        newMat = nasobeni(A,B)
    else:
        print("Matice není možno násobit")
        
    print(newMat)    

    




