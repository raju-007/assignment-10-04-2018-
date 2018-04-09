# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 14:37:59 2018

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
            
        print("String  actual value b is = "+b)
       
        print("String reversed value of c is = "+c)
   
        
        if c.lower()==b.lower():
            print("pallindrone")
        else:
            print("not pallindrone")
            
    
        

te=open("ban.txt","r+")
ka=te.readlines()            
print(ka)      
ob=stl()
for n in ka:
    ob.str1(n)
    
"""
Delimeter using newline
ban.txt file contain

nitin
malayalam
A man, a plan, a canal: Panama

"""


