#!/usr/bin/env python3

A = [[3,4,5,1],[1,2,1,2],[0,9,2,1],[3,4,55,2]]

def trans(A):
    OUT = []

    for j in range(len(A)):
        row = []
        for k in range(len(A[0])):
            row.append(A[k][j])
        OUT.append(row)

    # print(OUT)
    return OUT

if __name__ == "__main__":
    for y in range(len(A)):
        for x in range(len(A[0])):
            print(A[y][x],end='|')

        print()

    out = trans(A)

    for y in range(len(A)):
        for x in range(len(A[0])):
            print(out[y][x],end='|')

        print()
