#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 16:32:15 2020

@author: marla

function to return generator of n lines from a file
"""
import os
import string

tmp_path = os.getcwd()
filename = "alphabet.txt"



def read_n(filename, n):
'''
Function to read n lines from a file
Parameters:
	filename: name of the file
	n: number of lines to read
Returns: generator
'''
    f=open(filename,"r")
   # print("here")
   # print(f.readline())
    counter = 0
 
    ans=""
    for line in f:
        
        while counter<=n:
            counter +=1
            ans = ans + f.readline()
            

        print(ans)
        yield ans
        
        counter = 0
        ans = ""
    
  


i = read_n("sub/"+filename, 2)
print(i)
print(iter(i))
print(len(list(i)))

