#!/usr/bin/env python3

def makeMat(y,x):
    mat = []
    for yLoop in range(int(y)):
        radek=[]
        for xLoop in range(int(x)):
            radek.append(int(input("Zadejte hodnotu [{}][{}]: ".format(yLoop,xLoop))))
        mat += [radek]
    return mat

def matCompatibility(a,b):
    if(len(a[0]) == len(b)):
        return True
    else:
        return False

def nasobeni(a,b):
    mat = []
    for newy in range(len(a)):
        dopsat

    

if __name__ == "__main__":
    print("Vytváření matice A:\nZadejte počet sloupců a řádků oddělených čarou (y,x)")
    while True:
        try:
            y,x = input().split(',')
            break
        except:
            print("wrong!")
            
    A = makeMat(y,x)
    print(A)
    print(len(A[0]))

    print("Vytváření matice B:\nZadejte počet sloupců a řádků oddělených čarou (y,x)")
    while True:
        try:
            y,x = input().split(',')
            break
        except:
            print("wrong!")
    B = makeMat(y,x)
    print(B)
    print(len(B))

    fififi = matCompatibility(A,B)
    if(fififi):
        nasobeni(A,B)
    else:
        print("Matice není možno násobit")
    

    




