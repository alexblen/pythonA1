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
    for n in range(N):
        if Rt[n]==0:
            Rt1[n]=Rt[n-1]
        elif Rt[n]==1:
            if Rt[(n+1)%N]==0:
                Rt1[n]=0
            else:
                Rt1[n]=1
    return Rt1
            
x=[1,0,0,1,1,1,0,0,1]
y=updateR(x)


#part 2
NumCells=100
Rt0=np.zeros((NumCells,1))

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

for i in range(1,NumCells):
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

#question 2

#part 1
M=5
value=1
Traj = np.where(np.array(x) == value)[0]+1
Traj1= np.where(np.array(y) == value)[0]+1

#if i want a list can do
#Trajt=[i+1 for i,val in enumerate(x) if val==1]
 
    
def new_position(R,Traj):
    Trajt1=np.zeros_like(Traj)
    M=len(Traj)
    N=len(R)
    for m in range(M):
        num=Traj[m]
        if R[(num)%N]==1:
            Trajt1[m]=Traj[m]
        else:
            Trajt1[m]=Traj[m]+1
    return Trajt1

