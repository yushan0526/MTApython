# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 15:35:45 2021

@author: MTAEXAM
"""

#n階
n=int(input("n:"))

total=1
for n in range(1,n+1):
    total*=n
    
print(total)