#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 17:11:11 2020

@author: marla

Using f-strings to format output to look like a table; create class Item, add items to cart and print formatted list of items
"""
import json

class Cart:
    def __init__(self):
        #make this a dictionary with name as key; then can sort by names; will have to adjust list comprehensions
        self.items=[]
    
    def add(self, Item):
        self.items.append(Item)
    
    def __repr__(self):
        colWidth = max(len(item.name) for item in self.items)+2
        print(colWidth)
        header = ('No.' + (colWidth-len('No.')-1)*" " + 'Unit' + (colWidth-len('Unit'))*" " + 'Name' + (colWidth-len('Name'))*" " + "Cost" + (colWidth - len("Cost"))*" "+ "Total")
        formattedString = '\n'.join(str(item.quantity) + (colWidth-len(str(item.quantity)))*" " + item.measure + (colWidth-len(item.measure))*" " + item.name + (colWidth-len(item.name))*" " + "@" + str(item.price) + (colWidth-len(str(item.price)))*" " + "$" + str(item.price*item.quantity) for item in self.items)
        #formattedString = '\n'.join(str(item.quantity) + "   " + item.measure + "   "+ item.name + "   @" + str(item.price) + "   "+ str(item.quantity*item.price) for item in self.items)
        return header + "\n" + formattedString
    
    def __str__(self):
        formattedString = ''.join(item.name + ", " for item in self.items)
        formattedString = formattedString[:-2]
        return formattedString
    
    def __format__(self, format_spec):
        if format_spec=="short":
            return str(self)
        elif format_spec=="long":
            return repr(self)
    
class Item:
    def __init__(self, quantity, measure, name, price):
        self.quantity=quantity
        self.measure = measure
        self.name=name
        self.price=price
        
        
cart=Cart()
cart.add(Item(1.5,'kg','tomatoes',5))
cart.add(Item(2, 'kg', 'cucumbers', 4))
cart.add(Item(1, 'tube', 'toothpaste',2))
cart.add(Item(1, 'box', 'tissues',4))
print(f"Your cart contains: {cart:short}")
print(f"Your cart:\n {cart:long}")
    
