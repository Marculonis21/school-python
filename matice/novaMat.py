#!/usr/bin/env python3

def makeMat():
    print("Vytváření matice A:\nZadejte počet sloupců a řádků oddělených čarou (y,x)")
    while True:
        try:
            y,x = input().split(',')
            break
        except:
            print("wrong!")
    
    mat = []
    for yLoop in range(int(y)):
        radek=[]
        for xLoop in range(int(x)):
            radek.append(int(input("Zadejte hodnotu [{}][{}]: ".format(yLoop,xLoop))))
        mat += [radek]
    return mat

def rozsirena():
    print("Vytvářím rozšířenou matici:")
    print("Zadejte počet rovnic")
    while True:
        try:
            y = int(input())
            break
        except:
            print("wrong!")

    mat = []
    for yLoop in range(int(y)):
        radek=[]
        xx = (input("Zadejte koficienty v rovnici {} oddělených čarou (1,2,3,...): ".format(yLoop)).split(','))
        print(xx)
        radek += [int(x) for x in xx]
        mat += [radek]
        print(mat)
    return mat

def printMat(A, roz=False):
    for i in range(len(A)):
        print()
        if not(roz):
            print("|",end="")
        for x in range(len(A[0])):
            print("  {}".format(A[i][x]), end="")
            if(roz):
                if(x == len(A[0])-2):
                    print("  |", end="")
        if not(roz):
            print("  |",end="")
            

print()
                         
if __name__ == "__main__":
    A = rozsirena()
    printMat(A, True)
    printMat(A)
    pass
