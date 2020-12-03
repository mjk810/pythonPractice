#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 16:28:16 2020

@author: marla

Create magic tuples: tuples where all numbers within the tuple add to the same number
using a generator
"""


def magic_tuple1(tupleSum, numTuples):

    counter = 1
    while counter < numTuples:
        result =(counter, tupleSum-(counter))
        #print(result)
        yield result
        counter+=1
        
def magic_tuples(tupleSum, maxVal):
'''
Function to create the magic tuple
Parameters:
	tupleSum: the number that all ints in the tuple add to
	maxVal: the greatest number that can be in the tuple

'''
    for i in range(maxVal):
        if tupleSum-i<maxVal:
            result =(i, tupleSum-(i))
            #print(result)
            yield result

#Code to run it
for t in magic_tuples(10,10):
    print(t)

