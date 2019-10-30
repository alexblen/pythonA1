# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 10:33:33 2019

@author: s1983051
"""

import numpy as np
import matplotlib.pyplot as plt
#question 1
#part a
def updateR(Rt):
    '''
    this function takes a vector of car positions and returns the positions of those cars at t+1
    '''
    Rt1=np.zeros_like(Rt)
    N=len(Rt)
#    Rt[N]==Rt[0]
    for n in range(1,N):
        if np.array((Rt[n]==0, Rt[n-1]==0)).all():
            Rt1[n]=0
        elif np.array((Rt[n]==0, Rt[n-1]==1)).all():
            Rt1[n]=1
    for n in range(N-2):
        if np.array((Rt[n]==1, Rt[n+1]==0)).all():
            Rt1[n]=0
        elif np.array((Rt[n]==1, Rt[n+1]==1)).all():
            Rt1[n]=1
    if np.array((Rt[N-1]==1, Rt[0]==0)).all():
        Rt1[N-1]=0
    if np.array((Rt[N-1]==1, Rt[0]==1)).all():
        Rt1[N-1]=1
    if np.array((Rt[0]==0, Rt[N-1]==0)).all():
        Rt1[0]=0
    if np.array((Rt[0]==0, Rt[N-1]==1)).all():
        Rt1[0]=1
    return Rt1
            
x=[1,0,0,1,1,1,0,0,1]
y=updateR(x)

#i need to improve part a to take into account the periodic boundary condition 
#is there a better way i can write the function than returning all the posibilities?

#part 2
Nb=100
Rt0=np.zeros((Nb,1))

def primes():
    '''
    Function uses the sieve of Eratosthenes method to return a list
    of primes <=100.
    '''
    prime_list = list(range(2,101))
    for number in prime_list:
        i = prime_list.index(number)
        for j in prime_list[i+1:]:
            if j%number==0:
                prime_list.remove(j)
    return prime_list

prime100=primes()

for i in range(1,Nb):
    if(i in prime100 or (i>40 and i<=55)):
        Rt0[i-1]=1

def updateRtimes(Rt,T):
    '''
    Function which takes our original vector and returns car positions at time T
    '''
    for t in range(T):
        Rt1=updateR(Rt)
        Rt=Rt1
    return Rt

#part 3
def PlotTimeIntervals(Rt0,t1,t2):
    '''
    calculates all the positions for the cars between t1 and t2
    then plots a checkerboard of where each car is at each time
    '''
    c=t2-t1
    Start_pos=updateRtimes(Rt0,t1)
    temp=Start_pos
    for t in range(c):
        updated=updateRtimes(Start_pos,t+1)
        temp=np.concatenate((temp,updated),axis=1)
    return plt.imshow(temp.T)

    
PlotTimeIntervals(Rt0,0,20)
PlotTimeIntervals(Rt0,300,320)
PlotTimeIntervals(Rt0,380,400)
