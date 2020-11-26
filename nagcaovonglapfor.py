# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 22:39:36 2020

@author: tanta
"""

list2 = [({'name': 'Peter', 'age':2}, {'name': 'John', 'age':21}), 
         ({'name': 'Mary', 'age':2}, {'name': 'Trandanpro', 'age':21}), 
         ({'name': 'Nam', 'age':2}, {'name': 'Hung', 'age':21}), 
         ({'name': 'Mai', 'age':2}, {'name': 'Loan', 'age':21})]
for z in list2:
    for y in z:
     print(y)
     for e,h in enumerate(y,1):
         print(e,h,":",y[h])

               