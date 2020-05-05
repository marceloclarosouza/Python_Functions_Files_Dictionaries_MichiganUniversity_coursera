# -*- coding: utf-8 -*-
"""
Created on Tue May  5 11:34:57 2020

@author: mcsbi
"""


list1 = [8, 3, 4, 5, 6, 7, 9]
accum = 0
i = 0
while i < len(list1):
      accum+= list1[i]
      i+=1

print(accum)