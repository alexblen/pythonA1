# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 10:33:33 2019

@author: s1983051
"""

import numpy as np
#question 1
#part a
def updateR(Rt):
#this function takes a vector of car positions and returns the positions of those cars at t+1
    Rt1=np.zeros_like(Rt)
    N=len(Rt)
#    Rt[N]==Rt[0]
    for n in range(N-1):
        if(Rt[n]==0 and Rt[n-1]==0):
            Rt1[n]=0
        elif (Rt[n]==0 and Rt[n-1]==1):
            Rt1[n]=1
    for n in range(N-2):
        if(Rt[n]==1 and Rt[n+1]==0):
            Rt1[n]=0
        elif(Rt[n]==1 and Rt[n+1]==1):
            Rt1[n]=1
    if(Rt[N-1]==1 and Rt[0]==0):
        Rt1[N-1]=0
    if(Rt[N-1]==1 and Rt[0]==1):
        Rt1[N-1]=1
#    if(Rt[0]==0 and Rt[N-1]==0):
#        Rt1[0]=0
#    if(Rt[0]==0 and Rt[N-1]==1):
#        Rt1[0]=1
    return Rt1
            
x=[1,0,0,1,1,1,0,0,1]
y=updateR(x)

#i need to improve part a to take into account the periodic boundary condition 
#is there a better way i can write the function than returning all the posibilities?

#part b
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
