# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 14:06:40 2019

@author: user
"""
import numpy as np
import numpy.linalg as la
from math import sqrt


#1.

#1a

a=np.array([1,1,0])
b=np.array([0,1,1])

res=(2 *a ) - (3 * b)

print(res)

#1b
c=np.concatenate((a, b))
print(c)


#1c
d=np.concatenate((a[1:2],b[1:3]))

print(d)

#d
edist=sqrt( ((a[0] - b[0]) **2) + ((a[1] - b[1]) **2) + ((a[2] - b[2]) **2) )
print(edist)
edist1=la.norm(a-b)
print(edist1)

x=a+b
y=a-b

angle=np.arccos( (x @ y)  / ( la.norm(x) * la.norm(y) ) )

angle_in_degrees=np.degrees(angle)

print(F"angle in redian { angle } and in degrees is { angle_in_degrees }")


##########Set 3



a=np.array([1,-1,0,1,3,2,3,-1,-4,4,1,0,1,1,-2]).reshape(3,5)

mean_by_colms=np.mean(a,axis=0)

std_by_colms=np.std(a,axis=0)


#dist=[la.norm((z - a[:,i:i+1])) for i in range(0,a.shape[1],1)]
#a[:,np.argmin(dist):np.argmin(dist)+1]
#min
#target point shown as z
z=np.array([1,1,1])
dist=10000000

for i in range(0,a.shape[1],1):
    p=a[:,i:i+1]
    norm=la.norm(p-z)
    if norm < dist:
        dist=norm
        nearest_point=p
        
print(F"NP is defined { nearest_point }")
    

#set 2

#a

ns=np.random.randint(-9999,9999,size=(3,3))
sym=(ns + ns.T) // 2
new_mat=sym[:,[0,2]][:3:2]
print(sym)
print(new_mat)

#skew-sym

ns=np.random.randint(-9999,9999,size=(3,3))
ssym=(ns + ns.T) // 2
new_mat=ssym[:,[0,2]][:3:2]
print(ssym)
print(new_mat)

#stochastic

ns=np.random.randint(1,999999,size=(3,3))
sum_of_ns=np.sum(ns)

stochastic = ns / sum_of_ns
#sum_of_stochastic = np.sum(stochastic)
#print(sum_of_stochastic)
new_mat=stochastic[:,[0,2]][:3:2]
print(stochastic)
print(new_mat)














































