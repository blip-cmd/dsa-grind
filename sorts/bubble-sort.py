#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    swaps = 0
    n = len(a)
    
    for i in range(n):
        for j in range(n-1): #n-1 to skip the last element since max_item bubbles up.
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]  #on the right side, python creates the tuple first before unpacking it, allowing swapping/multiple assignments on one line.
                swaps += 1
                
    print(f"Array is sorted in {swaps} swaps.")
    print(f"First Element: {a[0]}") 
    print(f"Last Element: {a[-1]}")
    

if __name__ == '__main__':
    # n = int(input().strip())

    # a = list(map(int, input().rstrip().split()))

    # countSwaps(a)
    
    #test the function with a sample input
    a = [6, 4, 1]
    countSwaps(a)
    
    
    
