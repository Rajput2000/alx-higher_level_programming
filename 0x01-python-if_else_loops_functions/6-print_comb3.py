#!/usr/bin/python3
for n in range(9):
    for j in range(1, 10):
        if j > n:
            if j != 9 or n != 8:
                print("{:d}{:d}, ".format(n, j), end="")
            else:
                print("{:d}{:d}".format(n, j))
