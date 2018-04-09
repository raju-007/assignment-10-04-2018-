# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 15:10:24 2018

@author: rajashekhar
"""

class stl:
    
    def str1(self,a):
        b=""
        c=""
        
      
        k=len(a)-1
        i=0
        
        while k>=0:
            if (a[i]>='a' and a[i]<='z') or (a[i]>='A' and a[i]<='Z') or (a[i]>='0' and a[i]<='9'):
                b=b+a[i]
                c=a[i]+c
            k-=1
            i+=1
            
        print("String  actual value= "+b)
       
        print("String reversed value of c is = "+c)
   
        if c.lower()==b.lower():
            print("pallindrone")
        else:
            print("not pallindrone")
           
ob=stl()
i=1

with open("input.txt") as fo:
    for rec in fo:
      ja=rec.split('#')[0]
      ra=rec.split('#')[1]
      print("input ="+str(i))
      ob.str1(ja)
      print("********")
      ob.str1(ra)
     
      i=i+1

"""
Delimeter using #

The input.txt file contain

A man, a plan, a canal: Panama # 9432112349
ma % la *   %$ ya!!! la %$ m  # 8765445678
"""

    
