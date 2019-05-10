# -*- coding: utf-8 -*-
"""
Created on Fri May 10 15:49:41 2019

@author: user
"""

class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
        
    def ShiftUp(self,i):
        while i // 2 > 0:
            if self.heapList[i][1] < self.heapList[i // 2][1]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2
    
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.ShiftUp(self.currentSize)
    
    def ShiftDown(self,i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i][1] > self.heapList[mc][1]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc
    
    def minChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2][1] < self.heapList[i*2+1][1]:
                return i * 2
            else:
                return i * 2 + 1
            
    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.ShiftDown(1)
        return retval
    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.ShiftDown(i)
            i = i - 1
            
myHeap=BinHeap()

with open("C:/Users/user/Desktop/jobs.txt") as file:
    data=file.readlines()
    
num=data[0]
startTime=data[1].split(',')
finishTime=data[2].split(',')

[ myHeap.insert((int(startTime[i]),int(finishTime[i]))) for i in range(int(num)) ]

prioq=[]

[ prioq.append(myHeap.delMin()) for item in range(int(num)) ]


for each in range(len(prioq)):
    if each != 0:
        if prioq[each - 1][1] > prioq[each][0]:
            pass
        else:
            print(prioq[each])
        
    else:
        print(prioq[each])

    
