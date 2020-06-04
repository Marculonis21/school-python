#!/usr/bin/env python3

A = [[1,0,1],[1,1,1]]
B = [[1,2],[5,1],[1,1]]

def nasobeni(A,B):
    if not (len(A[0]) == len(B)): return
    END = []

    for y in range(len(A)):
        radek = []
        for x in range(len(B[0])):
            s = 0
            for j in range(len(A[0])):
                s += A[y][j]*B[j][x]

            radek.append(s)

        END.append(radek)
    print(END)

if __name__ == "__main__":
    nasobeni(A,B)
