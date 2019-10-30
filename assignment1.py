# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 10:33:33 2019

@author: s1983051
"""

import numpy as np
#question 1
#part a
def updateR(Rt):
    Rt1=np.zeros_like(Rt)
    N=len(Rt)
    for n in range(1,N-1):
        if(Rt[n]==0 and Rt[n-1]==0):
            Rt1[n]=0
        elif (Rt[n]==0 and Rt[n-1]==1):
            Rt1[n]=1
    for n in range(N-2):
        if(Rt[n]==1 and Rt[n+1]==0):
            Rt1[n]=0
        elif(Rt[n]==1 and Rt[n+1]==1):
            Rt1[n]=1
    if(Rt[0]==0 and Rt[N-1]==0):
        Rt1[0]=0
    if(Rt[0]==0 and Rt[N-1]==1):
        Rt1[0]=1
    if(Rt[N-1]==1 and Rt[0]==0):
        Rt1[N-1]=0
    if(Rt[N-1]==1 and Rt[0]==1):
        Rt1[N-1]=1
    return Rt1
            
x=[1,0,0,1,1,1,0,0,1]

