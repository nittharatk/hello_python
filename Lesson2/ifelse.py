#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())


    #If n is odd, print Weird
    #print(5 % 3) #2
    #print(5 / 3) #1.67
    #print(5 // 3)#1
    
    
    if n % 2 == 1:
        print ("Weird")
    
    #If n is even and in the inclusive range of 2 to 5, print Not Weird
    
    if (n % 2 == 0) & (n >= 2) & (n <= 5):
        print ("Not Weird")
    
    #If n is even and in the inclusive range of 6 to 20 , print Weird
    if (n % 2 == 0) & (n >= 6) & (n <= 20):
        print ("Weird")
    
    #If n is even and greater than 20 , print Not Weird
    if (n % 2 == 0) & (n > 20):
        print ("Not Weird")

"""
    if n % 2 == 1:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")    
"""    