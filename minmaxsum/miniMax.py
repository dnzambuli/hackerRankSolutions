#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
class MinMax():
    def __init__(self, minimum, maximum):
        self.minimum = minimum
        self.maximum = maximum
    def __repr__(self):
        return '%d %d'%(self.minimum, self.maximum)
    
def sortArr(arr):
    lengthArr = len(arr)
    for i in range(0, lengthArr):
        for j in range(0, lengthArr-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1] , arr[j]

def miniMaxSum(arr):
    # Write your code here
    sortArr(arr)
    minSide = arr[:-1]
    maxSide = arr[1:]
    minSideSum = sum(minSide)
    maxSideSum = sum(maxSide)
    
    output = MinMax(minSideSum, maxSideSum)
    return output


