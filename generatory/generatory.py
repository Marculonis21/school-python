#!/usr/bin/env python3

import random

CATS = "Prvočísla,"

def prvocisla(n = 100):
    for i in range(1, n):
        delitele = 0
        for x in range(1, i+1):
            if(i%x == 0):           
                delitele += 1

        if(i != 1 and delitele == 2):
            yield i
        elif(i == 1):
            yield i

if __name__ == "__main__":
    while True:
        print("Co tu chceš?")
        for i in range(len(CATS.split(',')) - 1):
            print("{:<15} -> {}:".format(CATS.split(',')[i],i))
        inp = int(input())

        if(inp == CATS.split(',').index("Prvočísla")):
            length = random.randint(100,500)
            print("Prvočísla: 1 - {}".format(length))
            for pc in prvocisla(length):
                print(pc, end = ' ')

            print()
