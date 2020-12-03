#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 16:13:38 2020

@author: marla

class that inherits from dict; implement the __getitem__ method to allow for slices
"""

class SliceableDict(dict):
   
    def __getitem__(self, key):
        mylist = []
        if key not in self.keys():
            try:
                for item in key:
                    val = dict.__getitem__(self, item)
                    mylist.append(val)
            except TypeError as e:
                raise KeyError("no such key {}".format(key))
        else:
            mylist.append(dict.__getitem__(self, key))
        return mylist
        
    
        
        


d=SliceableDict(a=1,b=2,c=3)
print(len(d))
print(d['ab'])
print(d[('a','b')])
print(d['a'])
#print(d[123])
'''
d=SliceableDict()
d['a'] = 10
d['b'] = 20
d['c'] = 30
print(len(d))
print(d.keys())
print(d['a'])
print(list(d.items()))
print(list(d))
'''

