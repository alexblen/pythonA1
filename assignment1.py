import numpy as np
import matplotlib.pyplot as plt
import sympy as sympy
import random as rand
import scipy.stats as stats
#question 1
#part a
def updateR(R):
    '''
    this function takes a vector of car positions and returns the positions of those cars at t+1
    '''
    R_new=np.zeros_like(R)
    N=len(R)
    for n in range(N):
        if R[n]==0:
            R_new[n]=R[n-1]
        elif R[n]==1:
            if R[(n+1)%N]==0:
                R_new[n]=0
            else:
                R_new[n]=1
    return R_new
            

#part 2
NumCells=100
R_Prime=np.zeros((NumCells,1)).astype(int)

for i in range(1,NumCells):
    prime=sympy.isprime(i)
    if(prime==True or (i>40 and i<=55)):
        R_Prime[i-1]=1


def updateRtimes(R,T):
    '''
    Function which takes our original vector and returns car positions at time T
    '''
    for t in range(T):
        R_new_t=updateR(R)
        R=R_new_t
    return R

#part 3
def PlotTimeIntervals(R,t1,t2):
    '''
    calculates all the positions for the cars between t1 and t2
    then plots a checkerboard of where each car is at each time
    '''
    c=t2-t1
    Start_pos=updateRtimes(R,t1)
    temp=Start_pos
    for t in range(c):
        updated=updateRtimes(Start_pos,t+1)
        temp=np.concatenate((temp,updated),axis=1)
    plt.imshow(temp.T)
    plt.show()

    
PlotTimeIntervals(R_Prime,0,20)
PlotTimeIntervals(R_Prime,300,320)
PlotTimeIntervals(R_Prime,380,400)




#question 2

#part 1


#if i want a list can do
#Trajt=[i+1 for i,val in enumerate(x) if val==1]
 
    
def new_position(R,Traj):
    '''
    Takes the trajectory at t and returns the trajectory at t+1
    '''
    M=len(Traj[:,-1])
    N=len(R)
    Traj_new=np.zeros((M,1)).astype(int)
    for m in range(M):
        num=Traj[m,-1]
        if R[(num)% N]==1:
            Traj_new[m]=Traj[m,-1]
        else:
            Traj_new[m]=Traj[m,-1]+1
    return Traj_new

def new_updateR(Traj_t1,N):
    '''
    takes the trajectory at t+1 and the number of cells in the original vector and returns the car positions
    '''
    R=np.zeros((N,1)).astype(int)
    for t in range(len(Traj_t1)):
        j=Traj_t1[t]%N
        R[j-1]=1
    return R

def ave_vel(Traj,t):
    '''
    tells us the speed at which a car is moving
    '''
    speed=Traj[:,t]-Traj[:,t-1]
    return sum(speed)/len(Traj[:,t])
    

        
#part 1
    
#VALLUES FOR TESTING
x=np.array((1,0,0,1,1,1,0,0,1)).reshape(9,1)
x1=updateR(x)
x2=updateR(x1)
Traj_x = np.array((1,4,5,6,9)).reshape(5,1)
Traj_1=new_position(x,Traj_x)
Traj_2=new_position(x1,Traj_1)
Traj_3=new_position(x2,Traj_2)
np.concatenate((Traj_x,Traj_1,Traj_2,Traj_3),axis=1)

#Part 2

def create_Traj_t(R):
    '''
    takes R and returns the trajectory
    '''
    N=len(R)
    M=np.sum(R)
    i=0
    Traj=np.zeros((M,1)).astype(int)
    for n in range(N):
        if R[n]==1:
            Traj[i]=n+1
            i+=1
    return Traj
    

def create_Traj(R,Traj,T):
    '''
    takes a traj vector and spits out a matrix of all the trajectories from 1 to T
    '''
    R_temp=R
    Traj_temp=Traj
    Traj_matrix=Traj_temp
    for t in range(T):
        Traj_temp=new_position(R_temp,Traj_temp)
        R_temp=updateR(R_temp)
        Traj_matrix=np.concatenate((Traj_matrix,Traj_temp),axis=1)
    return Traj_matrix
    
def plot_ave_speed(R,Traj_2,T_2):
    Traj_matrix=create_Traj(R,Traj_2,T_2)
    Speed=np.zeros((T_2,1))
    steady_speed=0
    for t in range(1,T_2):
        Speed[t]=ave_vel(Traj_matrix,t)
        if Speed[t]>steady_speed:
            time_to_steady=t
            steady_speed=Speed[t]
    xgrid=np.linspace(1,T_2,T_2).astype(int)
    fig = plt.figure()
    fig1=plt.plot(xgrid,Speed,'k-')
    axes = plt.gca()
    axes.set_ylim([0, 1.1])
    return time_to_steady, steady_speed
    
#PART 3
rand.seed=2
def create_first_M_cells(M_2,N_2):
    Temp=np.concatenate((np.ones((M_2,1)),np.zeros((N_2-M_2,1))))   
    Temp=Temp.astype(int)
    return Temp

R_test_2=create_first_M_cells(15,50)
Traj_test_2=create_Traj_t(R_test_2)
plot_ave_speed(R_test_2,Traj_test_2,50)

R_test_3=create_first_M_cells(25,50)
Traj_test_3=create_Traj_t(R_test_3)
plot_ave_speed(R_test_3,Traj_test_3,50)

R_test_4=create_first_M_cells(35,50)
Traj_test_4=create_Traj_t(R_test_4)
plot_ave_speed(R_test_4,Traj_test_4,50)


#NEED TO ADD FIGURE NAME ETC
#what time does it level out at??


#Part 4
M=20
R_test_5=create_first_M_cells(M,50)
Traj_test_5=create_Traj_t(R_test_5)
plot_ave_speed(R_test_5,Traj_test_5,50)

Traj_test_6=sorted(rand.sample(range(0,50),M))
Traj_test_6=np.array(Traj_test_6).reshape(M,1)
R_test_6=new_updateR(Traj_test_6,50)
plot_ave_speed(R_test_6,Traj_test_6,50)

Traj_test_7=np.array((1,2,4,5,7,8,10,11,13,14,16,17,19,20,22,23,25,26,28,29)).reshape(20,1)
R_test_7=new_updateR(Traj_test_7,50)
plot_ave_speed(R_test_7,Traj_test_7,50)

#PART 4
#WITH m=30
M=30
R_test_5b=create_first_M_cells(M,50)
Traj_test_5b=create_Traj_t(R_test_5b)
plot_ave_speed(R_test_5b,Traj_test_5b,50)

Traj_test_6b=sorted(rand.sample(range(0,50),M))
Traj_test_6b=np.array(Traj_test_6b).reshape(M,1)
R_test_6b=new_updateR(Traj_test_6b,50)
plot_ave_speed(R_test_6b,Traj_test_6b,50)

Traj_test_7b=np.array((1,2,4,5,7,8,10,11,13,14,16,17,19,20,22,23,25,26,28,29,31,32,34,35,37,38,40,41,43,44)).reshape(M,1)
R_test_7b=new_updateR(Traj_test_7b,50)
plot_ave_speed(R_test_7b,Traj_test_7b,50)


#THEY ALL GET TO THE SAME LIMIT WHERE THEY ARE AS SPREAD OUT AS POSSIBLE

#PART 6
def Ave_Vel_Bern(N):
    P=np.linspace(0.2,0.8,10)
    speed=np.zeros(10)
    i=0
    for p in P:
        cars=stats.bernoulli.rvs(p,size=N)
        Traj1=create_Traj_t(cars)
        Traj=create_Traj(cars,Traj1,200)
        speed[i]=ave_vel(Traj,200)
        i+=1
    plt.plot(P,speed,'ko')
    plt.show()

Ave_Vel_Bern(800)

#PART 7
Ave_Vel_Bern(50)
Ave_Vel_Bern(2000)

#QUESTION 2C!!!!!!!!!!!!!!!
N=100
R_Prime_Fast=np.zeros((N,1)).astype(int)
for i in range(1,N):
    prime=sympy.isprime(i)
    if(prime==True or (i>60 and i<=85)):
        R_Prime_Fast[i-1]=1

def compute_Velocity(R):
    '''
    takes positions R and tells you the speed the car is going
    '''
    Traj=create_Traj_t(R)
    M=len(Traj)
    N=len(R)
    vel=np.zeros((M,1)).astype(int)
    for m in range(M):
        if R[Traj[m]%N]==1:
            vel[m]=0
        elif R[Traj[m]%N]==0 and R[(Traj[m]+1)%N]==1:
            vel[m]=1
        else:
            vel[m]=2
    return Traj, vel


def new_position2(R,Traj,Vel):
    '''
    takes R,Traj and Vel and spits out the new R vector
    '''
    Traj_new=Traj+Vel
    N=len(R)
    R_new=new_updateR(Traj_new,N)
    return R_new

vel=compute_Velocity(R_Prime_Fast)[1]
Traj_prime=compute_Velocity(R_Prime_Fast)[0] 
new_position2(R_Prime_Fast,Traj_prime,vel)


def fast_updateRtimes(R,T):
    '''
    Function which takes our original vector and returns car positions at time T
    '''
    for t in range(T):
        Traj=compute_Velocity(R)[0]
        Vel=compute_Velocity(R)[1]
        R_new_t=new_position2(R,Traj,Vel)
        R=R_new_t
    return R

def Fast_PlotTimeIntervals(R,t1,t2):
    '''
    calculates all the positions for the cars between t1 and t2
    then plots a checkerboard of where each car is at each time
    '''
    c=t2-t1
    Start_pos=fast_updateRtimes(R,t1)
    temp=Start_pos
    for t in range(c):
        updated=fast_updateRtimes(Start_pos,t+1)
        temp=np.concatenate((temp,updated),axis=1)
    plt.imshow(temp.T)
    plt.show()
    
#PART 2
def Fast_Slow_Compute_Velocity(R):
    '''
    takes positions R and tells you the speed the car is going
    '''
    Traj=create_Traj_t(R)
    M=len(Traj)
    N=len(R)
    vel=np.zeros((M,1)).astype(int)
    for m in range(M-1):
        if R[Traj[m]%N]==1:
            vel[m]=0
        elif R[Traj[m]%N]==0 and R[(Traj[m]+1)%N]==1:
            vel[m]=1
        else:
            vel[m]=2
    if R[Traj[M-1]%N]==1:
        vel[M]=0
    else:
        vel[M-1]=1
    return Traj, vel
    

def fast_slow_updateRtimes(R,T):
    '''
    Function which takes our original vector and returns car positions at time T
    '''
    for t in range(T):
        Traj=Fast_Slow_Compute_Velocity(R)[0]
        Vel=Fast_Slow_Compute_Velocity(R)[1]
        R_new_t=new_position2(R,Traj,Vel)
        R=R_new_t
    return R

def Fast_Slow_PlotTimeIntervals(R,t1,t2):
    '''
    calculates all the positions for the cars between t1 and t2
    then plots a checkerboard of where each car is at each time
    '''
    c=t2-t1
    Start_pos=fast_slow_updateRtimes(R,t1)
    temp=Start_pos
    for t in range(c):
        updated=fast_slow_updateRtimes(Start_pos,t+1)
        temp=np.concatenate((temp,updated),axis=1)
    plt.imshow(temp.T)
    plt.show()
    
Fast_Slow_PlotTimeIntervals(R_Prime_Fast,0,60)






#creating vectors to test (using the example in class)
M=5
x=np.array((1,0,0,1,1,1,0,0,1)).reshape(9,1)
x1=updateR(x)
x2=updateR(x1)
y_10updates=updateRtimes(x,9)
Traj_x = np.array((1,4,5,6,9)).reshape(5,1)
Traj_y=new_position(x,Traj_x)
Traj_matrix=np.concatenate((Traj_x,Traj_y),axis=1)
vel_car=ave_vel(Traj_matrix,1)

x
x1
y_10updates
Traj_x
Traj_y
Traj_matrix
vel_car

 
#def primes():
#    '''
#    Function uses the sieve of Eratosthenes method to return a list
#    of primes <=100.
#    '''
#    prime_list = list(range(2,101))
#    for number in prime_list:
#        i = prime_list.index(number)
#        for j in prime_list[i+1:]:
#            if j%number==0:
#                prime_list.remove(j)
#    return prime_list
#prime100=primes()


#DONT NEED
#(def plot_ave_speed(R,Traj_2,T_2):
    '''
    This puts M cars in the first cells of N rows
    Then returns plot of the cars speed at time T
    '''
    Temp=R
    Speed=np.zeros((T_2,1))
    steady_speed=0
    for t in range(T_2):
        R=updateRtimes(Temp,t)
        Traj_new_2=new_position(R,Traj_2)
        Traj_matrix=np.concatenate((Traj_2,Traj_new_2),axis=1)
        Speed[t]=ave_vel(Traj_matrix,1)
        Traj_2=Traj_new_2
        if Speed[t]>steady_speed:
            time_to_steady=t+1
            steady_speed=Speed[t]
    xgrid=np.linspace(1,T_2,T_2).astype(int)
    fig = plt.figure()
    fig1=plt.plot(xgrid,Speed,'k-')
    axes = plt.gca()
    axes.set_ylim([0, 1.1])
    return time_to_steady)

